from django.contrib import admin
from post_app.models import *
# Register your models here.
admin.site.register(category)
admin.site.register(forum_category)
admin.site.register(post)
admin.site.register(Comments)