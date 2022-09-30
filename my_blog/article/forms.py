# 引入表单类
from django import forms
# 引入文章模型
from .models import ArticlePost

# 写文章的表单类(ModelForm:适合与数据库交互（eg：新建、更新数据库字段）/Form：适合不与数据库交互)
class ArticlePostForm(forms.ModelForm):
    class Meta:
        # 指明数据模型来源
        model = ArticlePost
        # 定义表单包含的字段
        fields = ('title', 'body')