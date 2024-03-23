from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.


class TableRow(models.Model):
    table = models.ForeignKey('Table', related_name='rows', on_delete=models.CASCADE)

class TableCell(models.Model):
    content = models.TextField()
    row = models.ForeignKey(TableRow, related_name='cells', on_delete=models.CASCADE)

class Table(models.Model):
    page_item = models.ForeignKey('PageItem', related_name='tables', on_delete=models.CASCADE)

class Content(models.Model):
    text = models.TextField()
    table = models.ForeignKey(Table, related_name='contents', on_delete=models.CASCADE, null=True, blank=True)

class PageItem(models.Model):
    page = models.ForeignKey('Page', related_name='items', on_delete=models.CASCADE)
    content = models.ForeignKey(Content, related_name='page_items', on_delete=models.CASCADE)

class Page(models.Model):
    title = models.CharField(max_length=30)
    content = models.ForeignKey(Content, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title



class Schedule(models.Model):
    pass


# class User(AbstractUser):
#     pass
