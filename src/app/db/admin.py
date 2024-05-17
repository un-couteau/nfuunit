from django.contrib import admin

from .models import Page, SubPage, News
from mptt.admin import MPTTModelAdmin

@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
    readonly_fields = ('slug',)

@admin.register(SubPage)
class SubPageAdmin(MPTTModelAdmin):
    list_display = ('title', 'slug', 'page')
    raw_id_fields = ('page',)
    search_fields = ('title', 'content',)

    class Meta:
        verbose_name = 'Подстраница'
        verbose_name_plural = 'Подстраницы'

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'image', 'text')
    search_fields = ('title', 'text',)
    list_filter = ('title',)
    ordering = ('-id',)
