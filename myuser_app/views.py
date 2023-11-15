from django.shortcuts import render,redirect
from .models import MyUser
from post_app.models import post,Comments
from django.contrib.auth.decorators import login_required
# Create your views here.
from .forms import ProfileSettingsForm,ProfileAuthSettings
import asyncio
from django.contrib import messages
from asgiref.sync import sync_to_async,async_to_sync




# email
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.encoding import force_bytes,force_str
from django.contrib.auth.tokens import default_token_generator
from myuser_app.tokens import email_change_token
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
import asyncio




def profile_detail(request,username):
    user = MyUser.objects.filter(username = username).first()
    user_post = post.objects.filter(author_user = user)
    # for test in user_post:
    #     user_likes = MyUser.objects.filter(likes = test).exists()
    
    # print('userlşkike',user_likes)
    if user:

        context = dict(
            user = user,
            user_post = user_post,
            # user_likes = user_likes,
        )
        return render(request,'profile_detail.html',context)
    else:
        return redirect('404')
@login_required(login_url='login2')
def usersettings(request):
    if request.method == 'POST':
        form = ProfileSettingsForm(request.POST,request.FILES,instance=request.user)
        if form.is_valid() :
            print('hatayok',form.errors)
            form.save()
            return redirect('usersettings')
        else:
            print('form valid deil')
            print(form.errors)
            return redirect('usersettings')
    else:
        user = MyUser.objects.filter(id = request.user.id).first()
        if user:
            p = ProfileSettingsForm(instance=user)
            context = dict(
                user = user,
                settings = p,
            )
        else:
            return redirect('/')
        return render(request,'profilesettings.html',context)
@login_required(login_url='login2')
def userauthsettings(request):
    user = MyUser.objects.filter(id = request.user.id).first()
    inital_data = {
        'email': user.email
    }
    context = dict(
        email = ProfileAuthSettings(initial=inital_data)
    )
    return render(request,'userauthsettings.html',context)



@sync_to_async
def emailchangeactivate(request,uidb64,token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = MyUser.objects.get(pk = uid)
    except(TypeError,ValueError,OverflowError,MyUser.DoesNotExist):
        user = None
    if user is not None and email_change_token.check_token(user,token):
        user.email_active = False
        user.save()
        context = dict(
            user = user
        )
        return render(request,'emailchange.html',context)
    else:
        context = dict(
            error = 'error'
        )
        return render(request,'emailchange.html',context)


@sync_to_async
def sendemailchange(request,user):
    current_site = get_current_site(request)
    mail_subject = "E-postanızı onaylayın"
    message = render_to_string('sendemail.html',{
        'user':user,
        'domain': current_site.domain,
        'uid':urlsafe_base64_encode(force_bytes(user.pk)),
        'token': email_change_token.make_token(user),
    })
    send_mail(mail_subject, message, settings.EMAIL_HOST_USER, [user.email])




def emailchange(request):
    if request.method == 'POST':
        usermail = ProfileAuthSettings(request.POST,instance=request.user)
        user = MyUser.objects.filter(username = request.user.username).first()
        if usermail.is_valid():
            cleaneddata = usermail.cleaned_data.get('email')
            print('emial',user.email ,cleaneddata)
            if not user.email == cleaneddata:
                user.email = cleaneddata
                user.email_active = True
                user.save()
                asyncio.run(sendemailchange(request,user))               
                return redirect('/')
            else:
                return redirect('login2')
    else:
        return redirect('404')