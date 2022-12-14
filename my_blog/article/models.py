from django.db import models
# 导入内建的User模型。
from django.contrib.auth.models import User
# timezone 用于处理时间相关事务。
from django.utils import timezone
# 重定向
from django.urls import reverse

# 博客文章数据模型
class ArticlePost(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    body = models.TextField()
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True)
#     浏览量
    total_views = models.PositiveIntegerField(default=0)
    
    class Meta:
        ordering = ('-created',)
        
    def __str__(self):
        return self.title

    # 重定向：获取文章地址
    def get_absolute_url(self):
        return reverse('article:article_detail', args=[self.id])
