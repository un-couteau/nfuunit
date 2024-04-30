from db.models import Page, SubPage
from django.shortcuts import get_object_or_404
from django.shortcuts import render


def home(request):
    return render(request, 'main/index.html')


def page(request, page_slug):
    page = get_object_or_404(Page, slug=page_slug)
    context = {'page': page}
    return render(request, 'main/index.html', context)


def subpage(request, page_slug, subpage_slug):
    subpage = get_object_or_404(SubPage, slug=subpage_slug)
    context = {'page': subpage}

    return render(request, 'main/index.html', context)
