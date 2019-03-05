from django.contrib import admin
from .models import Post,Category,Tag

#定制admin页面
class Postadmin(admin.ModelAdmin):
    list_display = [
        'title',
        'created_time',
        'modified_time',
        'category',
        'author',
    ]
#注册模型
admin.site.register(Post,Postadmin)
admin.site.register(Category)
admin.site.register(Tag)

# Register your models here.
