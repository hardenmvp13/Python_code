from django.db import models
from django.utils.six import python_2_unicode_compatible

@python_2_unicode_compatible   # 装饰器用于兼容 Python2
class Comment(models.Model):
    #评论人的名字
    name = models.CharField(max_length=50)
    #评论的内容
    text = models.TextField()
    #评论的时间
    created_time = models.DateTimeField(auto_now_add=True)  #当评论数据保存到数据库时，自动把 created_time 的值指定为当前时间
    #被评论的文章
    post = models.ForeignKey("blog.Post")
    def __str__(self):
        return self.text[:20]
