from django.contrib import admin

from .models import Page, SubPage


@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
    # prepopulated_fields = {'slug': ('title',)}
    readonly_fields = ('slug',)


@admin.register(SubPage)
class SubPageAdmin(admin.ModelAdmin):
    list_display = ('title', 'page', 'slug')
    raw_id_fields = ('page',)
    search_fields = ('title', 'content',)

    class Meta:
        verbose_name = 'Страница'
        verbose_name_plural = 'Страницы'
