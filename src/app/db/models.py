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

    class Meta:
        verbose_name = 'Страница'
        verbose_name_plural = 'Страницы'


class SubPage(models.Model):
    title = models.CharField(max_length=100, unique=True, verbose_name='Заголовок/SLUG')
    slug = AutoSlugField(populate_from=get_slug_from_title, unique=True, blank=True, overwrite=True)
    content = CKEditor5Field(verbose_name='Содержимое', config_name='extends')
    page = models.ForeignKey(Page, on_delete=models.CASCADE, verbose_name='Страница', related_name='subpages')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Подстраница'
        verbose_name_plural = 'Подстраницы'


class News(models.Model):
    title = models.CharField(max_length=200, verbose_name='Заголовок')
    image = models.ImageField(upload_to='news_images/', verbose_name='Изображение')
    text = models.TextField(verbose_name='Текст')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
