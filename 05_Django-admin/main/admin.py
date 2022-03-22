from django.contrib import admin
from .models import Article, ArticleSeries

# Register your models here.
admin.site.register(ArticleSeries)
admin.site.register(Article)