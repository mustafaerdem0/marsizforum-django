from django.shortcuts import render,redirect
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from post_app.models import *
# Create your views here.


def index_views(request):
    context = dict(
        post = post.objects.all(),
        categorys = category_title.objects.all(),
        category_views = category.objects.all()
    )
    
    return render(request,'index.html',context)

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
                # print(username,email,password)
                createuser = MyUser.objects.create_user(username=username,email=email,password=password)
                if createuser:
                    message = "Kayıt başarılı giriş yapın"
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
    post = request.POST
    usernameoremail = post.get('usernameoremail')
    loginpassword = post.get('loginpassword')
    result = True
    message = ""
    if usernameoremail and loginpassword:    
        usernameauth = authenticate(username = usernameoremail, password = loginpassword)
        emailauth = MyUser.objects.filter(email = usernameoremail).first()
        if emailauth:
            user = MyUser.check_password(emailauth,loginpassword)
            if user:
                login(request,emailauth)
                print('emaille giriş yaptı')
                message = "Email ile giriş yaptınız hoşgeldin {user}".format(user = emailauth)
            else:
                result = False
                message = "e posta veya şifreniz yanlış tekrar deneyiniz"
        elif usernameauth:
                login(request,usernameauth)
                print("username ile giriş yaparsa",usernameauth)
                message = "Giriş başarılı username ile giriş yaptın hoşgeldin {user}".format(user = usernameauth)
        else:
            result = False
            message = "Kullanıcı adınız veya şifreniz yanlış tekrar deneyiniz"
            
    else:
        result = False
        message = "Boş bırakma"
    return JsonResponse({"result": result, "message":message})



def logout_forum(request):
    logout(request)
    return redirect('/')