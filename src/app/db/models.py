from django.db import models
from django_ckeditor_5.fields import CKEditor5Field
from django_extensions.db.fields import AutoSlugField
from pytils.translit import slugify


# Create your models here.
def get_slug_from_title(instance):
    return slugify(instance.title)


class Page(models.Model):
    title = models.CharField(max_length=100, unique=True, verbose_name='Заголовок/SLUG')
    slug = AutoSlugField(populate_from=get_slug_from_title, unique=True, blank=True,
                         overwrite=True)  # slug = AutoSlugField(populate_from='title', allow_unicode=True, unique=True, editable=True, blank=True)
    content = CKEditor5Field(verbose_name='Содержимое', config_name='extends')

    def __str__(self):
        return self.title


class SubPage(models.Model):
    title = models.CharField(max_length=100, unique=True, verbose_name='Заголовок/SLUG')
    slug = AutoSlugField(populate_from=get_slug_from_title, unique=True, blank=True, overwrite=True)
    content = CKEditor5Field(verbose_name='Содержимое', config_name='extends')
    page = models.ForeignKey(Page, on_delete=models.CASCADE, verbose_name='Страница', related_name='subpages')

    def __str__(self):
        return self.title
