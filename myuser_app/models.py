from django.db import models
from django.contrib.auth.models import AbstractUser
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
    class Meta:
        verbose_name = 'MyUser'
        verbose_name_plural = 'MyUsers'
