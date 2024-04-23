from asyncio import iscoroutinefunction

from asgiref.sync import sync_to_async
from db.models import Page, NavMenu
from django.db.models import Exists, OuterRef
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def nav_menu(func):
    async def wrapper(request: HttpRequest, *args, **kwargs) -> HttpResponse:
        pages = await sync_to_async(list, thread_sensitive=True)(Page.objects.all())

        pages_subquery = Page.objects.filter(item_id=OuterRef('pk')).values('id')
        nav_menu_items = await sync_to_async(list, thread_sensitive=True)(
            NavMenu.objects.annotate(has_pages=Exists(pages_subquery)).values('id', 'slug', 'has_pages', 'value'))

        if iscoroutinefunction(func):
            context = await func(request, *args, **kwargs)
        else:
            context = await sync_to_async(func, thread_sensitive=True)(request, *args, **kwargs)

        context['nav_menu_items'] = nav_menu_items
        context['pages'] = pages
        return await sync_to_async(render, thread_sensitive=True)(request, context['template'], context)

    return wrapper


@nav_menu
async def home(request: HttpRequest) -> HttpResponse:
    return {'template': 'main/index.html'}


@nav_menu
async def page(request: HttpRequest, page_slug) -> HttpResponse:
    return {'template': 'main/page.html'}


@nav_menu
async def content(request: HttpRequest, page_slug, content_slug) -> HttpResponse:
    return {'template': 'main/content.html'}
