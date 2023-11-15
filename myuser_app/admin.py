from django.contrib import admin
from .models import MyUser,Rank,OldEmail
# Register your models here.

admin.site.register(MyUser)
admin.site.register(Rank)
admin.site.register(OldEmail)