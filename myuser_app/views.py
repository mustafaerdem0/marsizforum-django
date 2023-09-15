from django.shortcuts import render
from .models import MyUser
from post_app.models import post,Comments
# Create your views here.


def profile_detail(request,username):
    user = MyUser.objects.filter(username = username).first()
    user_post = post.objects.filter(author_user = user)
    print(user_post)
    context = dict(
        user = user,
        user_post = user_post
    )
    return render(request,'profile_detail.html',context)
    