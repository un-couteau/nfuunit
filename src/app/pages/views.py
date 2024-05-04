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


# def news(request):
#     news_list = Paginator(News.objects.all(), 9)
#     num_page = request.GET.get('page', 1)
#     page_obj = news_list.get_page(num_page)
#     return render(request, 'main/news.html', {'news_list': news_list})


def page(request, page_slug):
    page = get_object_or_404(Page, slug=page_slug)
    context = {'page': page}
    return render(request, 'main/index.html', context)


def subpage(request, page_slug, subpage_slug):
    subpage = get_object_or_404(SubPage, slug=subpage_slug)
    context = {'page': subpage}

    return render(request, 'main/index.html', context)
