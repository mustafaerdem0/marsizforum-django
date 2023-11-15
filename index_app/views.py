from django.shortcuts import render,redirect
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from post_app.models import *
from asgiref.sync import sync_to_async,async_to_sync
from myuser_app.views import sendemailchange
# Create your views here.

# email
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.encoding import force_bytes,force_str
from django.contrib.auth.tokens import default_token_generator
from myuser_app.tokens import account_activation_token,password_reset_token
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
import asyncio

from post_app.forms import CreatePost

def error404(request):
    return render(request,'404.html')


@sync_to_async
def Activate(request,uidb64,token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = MyUser.objects.get(pk = uid)

    except(TypeError,ValueError,OverflowError,MyUser.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user,token):
        print('user',user.email)
        user.is_active = True
        user.save()
        context = dict(
            uservar = user
        )
        return render(request,'email.html',context)
    else: 
        return render(request,'email.html')

@sync_to_async
def ActiveEmail(request,creatuser):
    current_site = get_current_site(request)
    mail_subject = "Hesabınızı Aktifleştirin"
    message = render_to_string('activate_account.html',{
        'user':creatuser,
        'domain': current_site.domain,
        'uid':urlsafe_base64_encode(force_bytes(creatuser.pk)),
        'token': account_activation_token.make_token(creatuser),

    })
    send_mail(mail_subject, message, settings.EMAIL_HOST_USER, [creatuser.email])

def login2(request):
    if not request.user.is_authenticated:

        return render(request,'login2.html')
    else:
        return redirect('/')

def index_views(request):
    forms = CreatePost()
    context = dict(
        post = post.objects.all(),
        categorys = category_title.objects.all(),
        category_views = category.objects.all(),
        forms = forms,
    )
    return render(request,'index.html',context)

@sync_to_async
def register_forum(request):
    # ajaxtan dönen post verilerini aldm
    post = request.POST 
    username = post.get('username') 
    email = post.get('email')
    password = post.get('password')
    result = True
    message = ""
    controluser = MyUser.objects.filter(username = username).first()
    controluseremail = MyUser.objects.filter(email = email).first()
    if not controluser:
        if not controluseremail:
            if username and email and password:
                createuser = MyUser.objects.create_user(username=username,email=email,password=password)
                if createuser:
                    message = "Kayıt başarılı giriş yapın"
                    createuser.is_active = False
                    createuser.save()
                    asyncio.run(ActiveEmail(request,createuser))
                else:
                    message = "bu kullanıcı adı var lütfen başka kullanıcı adını deneyin"
            else:
                message = "Boş bırakma"
                result = False
        else:
            result = False
            message = "Bu emaile kayıtlı zaten hesap var buradan giriş yapın"
    else:
         result = False
         message = "Bu kullanıcı adına ait kullanıcı var buradan giriş yapın"
    return JsonResponse({"result": result, "message":message})
def login_forum(request):
    if not request.user.is_authenticated:
        post = request.POST
        usernameoremail = post.get('usernameoremail')
        loginpassword = post.get('loginpassword')
        result = True
        message = ""
        if usernameoremail and loginpassword:
            user = MyUser.objects.filter(username=usernameoremail).first()
            if not user:
                user = MyUser.objects.filter(email=usernameoremail).first()
            if user and user.check_password(loginpassword):
                if user.is_active and user.email_active == False:
                    login(request, user)
                    print('Giriş başarılı')
                    message = "Hoş geldiniz, {user}".format(user=user)
                else:
                    if user.email_active == True:
                        asyncio.run(sendemailchange(request,user))
                        result = False
                        message = "E posta değişikliği algılandı lütfen onaylayın"
                    else:
                        result = False
                        message = "E-postanızı onaylamadınız. Lütfen e-postanızı kontrol edin ve onaylayın."
                        asyncio.run(ActiveEmail(request,user))
            else:
                result = False
                message = "Kullanıcı adı veya şifre yanlış. Tekrar deneyin."
        else:
            result = False
            message = "Boş bırakmayın."

        return JsonResponse({"result": result, "message": message})
    else:
        return redirect('/')
def logout_forum(request):
    logout(request)
    return redirect('/')


def passwordresetactivate(request,uidb64,token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = MyUser.objects.get(pk = uid)
    except(TypeError,ValueError,OverflowError,MyUser.DoesNotExist):
        user = None
    if user is not None and default_token_generator.check_token(user,token):
        context = dict(
            user = user
        )
        return render(request,'passwordresetactivate.html',context)

    else:
        context = dict(
            error = 'error'
        )
        return render(request,'passwordresetactivate.html',context)

def resetpassword(request):
    post = request.POST
    password = post.get('password')
    password2 = post.get('password2')
    user = post.get('user')
    result = True
    message = ""
    users = MyUser.objects.filter(username= user).first()
    if user:
        if password == password2:
            users.set_password(password)
            users.save()
            message = 'işlem başarılı'
            
        else:
            result = False
            message = 'şifreler eşleşmiyor'
    else:
        result = False
        message = 'hata'
    return JsonResponse({"result": result, "message": message})

def passwordactivate(request,user):
    current_site = get_current_site(request)
    mail_subject = "Şifrenizi Değiştirin"
    message = render_to_string('password_account.html',{
            'user':user,
            'domain': current_site.domain,
            'uid':urlsafe_base64_encode(force_bytes(user.pk)),
            'token': default_token_generator.make_token(user),

        })
    send_mail(mail_subject, message, settings.EMAIL_HOST_USER, [user.email])



def passwordresetemail(request):
    post = request.POST
    email = post.get('useremail')
    user = MyUser.objects.filter(email = email).first()
    if user:
        passwordactivate(request,user)
        print('başarılı',user)
    return render(request,'passwordreset.html',)


    