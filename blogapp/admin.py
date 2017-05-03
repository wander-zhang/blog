from django.contrib import admin
from blogapp.models import Article

# Register your models here.

# Register your models here.
@admin.register(Article)

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title',)


    class Media:
        # 在管理后台的HTML文件中加入js文件, 每一个路径都会追加STATIC_URL/
        js = (
            '/static/kindeditor/kindeditor-all.js',
            '/static/kindeditor/lang/zh_CN.js',
            '/static/kindeditor/config.js',
        )