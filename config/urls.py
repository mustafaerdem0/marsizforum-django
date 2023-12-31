"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static


from django.contrib import admin
from django.urls import path,include
from index_app.views import *
from .settings import *
from post_app.views import *
from myuser_app.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index_views,name="index"),
    path('forumlar/<slug:forum_slug>',forum_views,name='forum_views'),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('konular/<slug:konu_slug>/<int:id>',post_views,name='post_views'),
    path('user/<str:username>', profile_detail, name='profile_detail'),
    path('activate/<str:uidb64>/<str:token>/',Activate, name='Activate'),
    path('passwordresetactivate/<str:uidb64>/<str:token>/',passwordresetactivate, name='passwordresetactivate'),
    path('passwordreset',passwordresetemail, name='passwordreset'),
    path('login',login2, name='login2'),
    path('createpost',createpost,name='createpost'),
    path('createcomment/<id>',createcomment,name='createcomment'),
    path('hesap',usersettings,name='usersettings'),
    path('hesap/guvenlik',userauthsettings,name='userauthsettings'),
    path('emailchange',emailchange,name='emailchange'),
    path('emailchange/<str:uidb64>/<str:token>/',emailchangeactivate,name='emailchangeurl'),
    path('404',error404,name='404'),

    # LOGİN REGİSTER LOGOUT FORUM APİ 
    path('api/v1/register',register_forum,name="register"),
    path('api/v1/login', login_forum, name="login"),
    path('api/v1/logout_forum', logout_forum, name="logout"),
    path('api/v1/<likepost>/like',postlike,name="postlike"),
    path('api/v1/<comment>',commentlike,name="commentlike"),
    path('api/v1/passwordreset/',resetpassword,name='resetpassword'),
    path('chat/',include('chat.urls')),


    # THIRD PARTY URL
    path('tinymce/', include('tinymce.urls')),





] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
