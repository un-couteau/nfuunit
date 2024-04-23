from django.db import models
from django_extensions.db.fields import AutoSlugField


# Create your models here.

class NavMenu(models.Model): # главы для навигационного меню
    value = models.CharField(max_length=100)
    slug = AutoSlugField(populate_from='value', allow_unicode=True, unique=True)

    def __str__(self):
        return self.value


class Page(models.Model): # страница, привязанная к slug навигационного меню, описывает заголовок и содержимое
    title = models.CharField(max_length=100)
    slug = AutoSlugField(populate_from='title', allow_unicode=True, unique=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    item = models.ForeignKey(NavMenu, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title


class PageContent(models.Model):
    title = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    content = models.ForeignKey(Page, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title if self.title else ''
