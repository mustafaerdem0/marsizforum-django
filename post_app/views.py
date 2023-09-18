from django.shortcuts import render
from post_app.models import *
from myuser_app.models import Rank
# Create your views here.

def forum_views(request,forum_slug):
    forum_views = category_title.objects.filter(category_title = forum_slug).first()
    category_views = category.objects.filter(category_tag_slug = forum_slug).first()
    post_views = post.objects.filter(category__category_tag_slug = forum_slug)
    print(forum_views)
    print(category_views)
    print('post',post_views)
    
    context = dict(
        forum_category = forum_views,
        post_views = post_views,
        category_views = category_views,
    )
 
    return render(request,'forum_views.html',context)

def post_views(request,konu_slug,id):
    post_views = post.objects.filter(post_slug = konu_slug,id=id).first()

    post_views.post_view += 1
    post_views.save()
    print('yaptik 32' ,post_views.post_view)
    rank_views = Rank.objects.first()
    test = post_views.author_user.rank
    print('rankı nasıl alıooz',test)
    print(post_views.category)
    
    print('psotasdasd ',post_views)
    context = dict(
        post = post_views
    )
    return render(request,'post_detail.html',context)

