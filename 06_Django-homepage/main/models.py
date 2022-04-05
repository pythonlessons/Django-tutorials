from django.db import models
from django.utils import timezone
from tinymce.models import HTMLField
from django.template.defaultfilters import slugify
import os

# Create your models here.
class ArticleSeries(models.Model):
    title = models.CharField(max_length=200, null=False, blank=False, unique=True)
    subtitle = models.CharField(max_length=200, default='', blank=True)
    slug = models.SlugField("Series slug", null=False, blank=False, unique=True)
    published = models.DateTimeField('Date published', default=timezone.now)

    def __str__(self):
        return self.title

    class Meta:
        # otherwise we get "Article Series" in admin panel
        ordering = ['-published']
        verbose_name_plural = "Series"


class Article(models.Model):
    title = models.CharField(max_length=200, null=False, blank=False, unique=True)
    subtitle = models.CharField(max_length=200, default='', blank=True)
    # article_slug = models.SlugField("Article slug", default=slugify(title), null=False, blank=False, unique=True)
    # article_slug = models.SlugField("Article slug", default="", null=True, blank=True, unique=False)
    article_slug = models.SlugField("Article slug", max_length=100, null=False, blank=False, unique=True)
    content = HTMLField(blank=True, default="")
    notes = HTMLField(blank=True, default="")
    published = models.DateTimeField('Date published', default=timezone.now)
    modified = models.DateTimeField('Date modified', default=timezone.now)
    series = models.ForeignKey(ArticleSeries, default='', verbose_name="Series", on_delete=models.SET_DEFAULT)

    def __str__(self):
        return self.title

    @property
    def slug(self):
        return self.series.slug + "/" + self.article_slug

    class Meta:
        ordering = ['-published']
        verbose_name_plural = "Articles"