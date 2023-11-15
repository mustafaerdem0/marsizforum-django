from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
# Create your models here.
class Rank(models.Model):
    title = models.CharField((""), max_length=50)
    image = models.ImageField((""), upload_to='rankimage', height_field=None, width_field=None, max_length=None)
    def __str__(self):
        return self.title

class MyUser(AbstractUser):
    avatar = models.ImageField(("Avatar"), upload_to='avatar/', height_field=None, width_field=None, max_length=None,blank=True,null=True)
    banner = models.ImageField(("Banner"), upload_to='banner/', height_field=None, width_field=None, max_length=None,blank=True,null=True)
    rank = models.ManyToManyField(Rank, verbose_name=("Rankı"),blank=True,null=True)
    birthday = models.DateField(("Doğum Günü"), auto_now=False, auto_now_add=False,blank=True,null=True)
    location = models.CharField(("Yaşadığın Şehir"), max_length=50, blank=True,null=True)
    website = models.CharField(("Website"), max_length=50,blank=True,null=True)
    about = models.TextField(("Hakkında"),blank=True,null=True)
    likes = models.ManyToManyField("post_app.post", verbose_name=("Beğendiğim postlar"),related_name="mylikes")
    is_active = models.BooleanField(("Kullanıcı email doğrulama"),default=False)
    email_active = models.BooleanField(("Change email active"),default=False)
    oldemail = models.ManyToManyField("myuser_app.OldEmail", verbose_name=("Eski Emaillerim"),blank=True,null=True)
    class Meta:
        verbose_name = 'MyUser'
        verbose_name_plural = 'MyUsers'
    def user_profile_detail_url(self):
        return reverse(
            'profile_detail',
            kwargs={
                'username': self.username
            }
        )

class OldEmail(models.Model):
    user = models.ManyToManyField(MyUser, verbose_name=("eski mail sahibi"),blank=True,null=True,related_name="oldmailuser")
    oldmail = models.CharField(("Email"), max_length=50,blank=True,null=True)
    def __str__(self):
        return self.oldmail

