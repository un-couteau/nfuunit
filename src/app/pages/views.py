from db.models import Page, SubPage, News
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404
from django.shortcuts import render


def home(request):
    news_list = News.objects.all()[:3]
    return render(request, 'main/home.html', {'news_list': news_list})


def news(request):
    news_objects = News.objects.all()

    paginator = Paginator(news_objects, 3)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)

    return render(request, 'main/news.html', {'page_obj': page_obj})


def news_item(request, pk):
    news_detail = get_object_or_404(News, pk=pk)

    return render(request, 'main/news_item.html', {'news_detail': news_detail})



def page(request, page_slug):
    page = get_object_or_404(Page, slug=page_slug)
    context = {'page': page}
    return render(request, 'main/index.html', context)



def subpage(request, page_slug, subpage_slug):
    subpage = get_object_or_404(SubPage, slug=subpage_slug, page__slug=page_slug)
    context = {'subpage': subpage}
    return render(request, 'main/index.html', context)


def subsubpage(request, page_slug, subpage_slug, subsubpage_slug):
    subsubpage = get_object_or_404(SubPage, slug=subsubpage_slug, parent__slug=subpage_slug, parent__page__slug=page_slug)
    context = {'subpage': subsubpage}
    return render(request, 'main/index.html', context)


def subsubsubpage(request, page_slug, subpage_slug, subsubpage_slug, subsubsubpage_slug):
    subsubsubpage = get_object_or_404(SubPage, slug=subsubsubpage_slug, parent__slug=subsubpage_slug, parent__parent__slug=subpage_slug, parent__parent__page__slug=page_slug)
    context = {'subpage': subsubsubpage}
    return render(request, 'main/index.html', context)
