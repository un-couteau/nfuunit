from django.shortcuts import render


def home(request):
    return render(request, 'main/index.html')


def page(request, page_slug):
    return render(request, 'main/page.html')


def content(request, page_slug, content_slug):
    return render(request, 'main/content.html')
