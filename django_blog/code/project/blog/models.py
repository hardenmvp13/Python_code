from django.db import models
#记得要导入User模块
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.six import python_2_unicode_compatible

# Create your models here.

#建立分类的类（Category）
#继承models.Model
class Category(models.Model):
    '''新建分类名，长度设置成最大100字符串，数据结构为：charfield'''
    name = models.CharField(max_length=100)

#建立标签的类（Tag）
#继承models.Model
class Tag(models.Model):
    '''新建标签名，长度设置成最大50字符串,数据结构为：charfield'''
    name = models.CharField(max_length=50)

#建立文章的类（Post）
#继承models.Model
@python_2_unicode_compatible
class Post(models.Model):
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("blog:detail",kwargs={"pk":self.pk})

    objects = models.Manager()
    '''新建标题，长度设置成最大100字符串,数据结构为：charfield'''
    title = models.CharField(max_length=100)

    '''新建正文，数据结构为：textfield'''
    body = models.TextField()

    '''新建 创建时间和最后修改时间，数据结构为：datatimefield'''
    created_time = models.DateTimeField()
    modified_time = models.DateTimeField()

    '''新建 文章摘要，长度设置成最大100字符串,数据结构为：charfield
       指定 CharField 的 blank=True 参数值后就可以允许空值了
    '''
    #excerpt = models.CharField(max_length = 100)
    excerpt = models.CharField(max_length=100,blank=True)

    '''新建 分类，使用外键foreignkey ,一对多'''
    #category = models.CharField()
    category = models.ForeignKey(Category)

    '''新建 标签，使用外键manytomanyfield  ,多对多'''
    #tag = models.CharField()
    tag = models.ManyToManyField(Tag,blank=True)

    '''新建 作者，通过 ForeignKey 把文章和 User 关联了起来。(一开始忘记了导入User)
       文章作者，这里 User 是从 django.contrib.auth.models 导入的。
       django.contrib.auth 是 Django 内置的应用，专门用于处理网站用户的注册、登录等流程，
       User 是 Django 为我们已经写好的用户模型。
    '''
    author = models.ForeignKey(User)



