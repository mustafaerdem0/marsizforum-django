from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

from autoslug import AutoSlugField
from django.urls import reverse
from myuser_app.models import *
# Create your models here.
# Başlık olucak postun aciklamasi olucak richtext kategorisi olucak

class category(models.Model):
    category = models.CharField(("Kategori"), max_length=50)
    category_description = models.TextField(("Formun açıklaması"),default="forumun açıklaması boş")
    category_tag_slug = AutoSlugField(populate_from='category',unique=True,)
    category_icon = models.CharField(("Fontawesome icon only text"), max_length=50,default="fa fa-shield")
    def __str__(self):
        return self.category
    def total_post_views(self):
        total_views = 0
        for post in self.postcategory.all():
            total_views += post.post_view
        return total_views
    def forum_absolute_url(self):
        return reverse(
        'forum_views',
        kwargs = {
            "forum_slug": self.category_tag_slug
        }
        )
class category_title(models.Model):
    category_title = models.CharField(("Kategori Başlığı"), max_length=50)
    category = models.ManyToManyField(category, verbose_name=("Kategoriler"))
    category_slug = AutoSlugField(populate_from='category_title',unique=True,)
    def __str__(self) :
        return self.category_title

class post(models.Model):
    author_user = models.ForeignKey(MyUser, verbose_name=("Postu Atan Kişi"), on_delete=models.CASCADE,blank=True,null=True)
    title = models.CharField(("Konu başlığı"), max_length=50)
    category = models.ForeignKey(category, verbose_name=("Kategorini Seç"), on_delete=models.CASCADE, blank=True,null=True,related_name="postcategory")
    content = RichTextField(verbose_name="Yazınız")
    post_slug = AutoSlugField(populate_from='title',unique=True)
    post_created = models.DateTimeField(("Postun Oluşturulma tarihi"), auto_now_add=True)
    post_updated = models.DateTimeField(("Postun Oluşturulma tarihi"), auto_now=True)
    like = models.ManyToManyField("myuser_app.MyUser", verbose_name=("Begeni"),related_name="postlike")
    post_view = models.PositiveIntegerField(("Post Görüntülenme"),default=0)
    def __str__(self):
        return self.title
    def iliked(self,request):
        for likess in request.user.likes.all():
            return likess
        # ilike = post.objects.filter(self.like =  )
    def post_absolute_url(self):
        return reverse(
            'post_views',
            kwargs={
                'konu_slug': self.post_slug,
                'id': self.id
            }
            
        )
 
    def profile_detail_url(self):
        return reverse(
            'post_views',
            kwargs={
                'konu_slug': self.post_slug,
                'id': self.id
            }
            
        )

class Comments(models.Model):
    comment_author = models.ForeignKey(MyUser, verbose_name=("Yorumu yapan kişi"), on_delete=models.CASCADE)
    comment_post = models.ForeignKey(post, verbose_name=("Hangi Posta yapıldı"), on_delete=models.CASCADE,related_name="comments")
    comment_content = RichTextField(verbose_name="Yorumunuz")
    comment_like = models.ManyToManyField("myuser_app.MyUser", verbose_name=("yorum begeni"),related_name="commentlike")
    def __str__(self):
        return self.comment_author.username