from django.shortcuts import render,redirect
from post_app.models import *
from django.http import JsonResponse
from .forms import CreatePost,CreateComment
from django.contrib.auth.decorators import login_required

from myuser_app.models import Rank
# Create your views here.

def forum_views(request,forum_slug):
    forum_views = category_title.objects.filter(category_title = forum_slug).first()
    category_views = category.objects.filter(category_tag_slug = forum_slug).first()
    post_views = post.objects.filter(category__category_tag_slug = forum_slug)

    
    context = dict(
        forum_category = forum_views,
        post_views = post_views,
        category_views = category_views,
    )
 
    return render(request,'forum_views.html',context)

def post_views(request,konu_slug,id):
    post_views = post.objects.filter(post_slug = konu_slug,id=id).first()
    user_likes = MyUser.objects.filter(likes = post_views).exists()
    print(user_likes)
    post_views.post_view += 1
    post_views.save()
    rank_views = Rank.objects.first()
    test = post_views.author_user.rank
    comment = CreateComment()
    context = dict(
        post = post_views,
        user_likes = user_likes,
        comment = comment,
    )
    return render(request,'post_detail.html',context)

@login_required(login_url='login2')
def postlike(request,likepost):
    response = {}
    posts = post.objects.filter(id = likepost).first()
    poststrue = post.objects.filter(like = request.user, id = likepost).first()
    user = MyUser.objects.filter(id = request.user.id).first()
    if poststrue:
        posts.like.remove(request.user)
        user.likes.remove(posts)
        postallcount = posts.like.all().count()
        response['data'] = {"status":"true",'count': postallcount}
        return JsonResponse(response)
    else:
        posts.like.add(request.user)
        user.likes.add(posts)
        postallcount = posts.like.all().count()
        response['data'] = {"status":"false",'count': postallcount}
        return JsonResponse(response)
   



@login_required(login_url='login2')
def createpost(request):
    context = {}
    if request.method == 'POST':
        form = CreatePost(request.POST,request.FILES)
        if form.is_valid():
            f = form.save(commit=False)
            print(f)
            f.author_user = request.user
            f.post_view = 0
            f.save()
            return redirect('post_views',f.post_slug,f.pk)
        else:
            result = False
            print(form.errors,'form valid değil')
            message = f"FORM VALİD OLMADI{form.errors}"
            return redirect('/')

    else:
        forms = CreatePost()
        context = dict(
            forms = forms, 
        )
    return render(request,'createpost.html',context)

@login_required(login_url='login2')
def createcomment(request,id):
    if request.method == 'POST':
        print('ngelio',id)
        form = CreateComment(request.POST,request.FILES)
        if form.is_valid():
            p = post.objects.filter(id = id).first()
            f = form.save(commit=False)
            f.comment_author = request.user
            f.comment_post = p
            f.save()
            return redirect('post_views',p.post_slug,p.id)
    else:
        redirect('/')


@login_required(login_url='login2')
def commentlike(request,comment):
    response = {}
    c = Comments.objects.filter(id = comment).first()
    if c:
        t = Comments.objects.filter(comment_like = request.user,id = comment).first()
        if t:
            response['data'] = 'zaten var'
            c.comment_like.remove(request.user)
            c.save()
            return JsonResponse(response)
            
        else:
            print('yorum', c)
            response['data'] = 'begendi'
            c.comment_like.add(request.user)
            c.save()
            return JsonResponse(response)
    
