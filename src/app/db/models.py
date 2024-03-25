from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.

class PageItemList(models.Model):
    value = models.CharField(max_length=100)
    def __str__(self):
        return self.value

class Page(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    item = models.ForeignKey(PageItemList, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title
