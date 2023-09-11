from django.db import models
from ckeditor.fields import RichTextField
from autoslug import AutoSlugField
# Create your models here.
# Başlık olucak postun aciklamasi olucak richtext kategorisi olucak

class category(models.Model):
    category = models.CharField(("Kategori"), max_length=50)
    category_tag_slug = AutoSlugField(populate_from='category',unique=True,)
    def __str__(self):
        return self.category
class forum_category(models.Model):
    category_title = models.CharField(("Kategori Başlığı"), max_length=50)
    category = models.ManyToManyField(category, verbose_name=("Kategoriler"))
    category_slug = AutoSlugField(populate_from='category_title',unique=True,)

    def __str__(self) :
        return self.category_title
class post(models.Model):
    title = models.CharField(("Konu başlığı"), max_length=50)
    category = models.ForeignKey(category, verbose_name=("Kategorini Seç"), on_delete=models.CASCADE, blank=True,null=True)
    content = RichTextField()

