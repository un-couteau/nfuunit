from django.shortcuts import render

from db.models import Page, PageItemList

def index(request):
    pages = Page.objects.all()
    pages_item_list = PageItemList.objects.all()
    page_items_with_pages = [{
        'page_item': page_item,
        'has_pages': pages.filter(item_id=page_item.id).exists()
    } for page_item in pages_item_list]
    return render(request, 'main/index.html', {'pages': pages, 'page_items_with_pages': page_items_with_pages})

def main(request):
    return render(request, 'main/main.html')


def about(request):
    return render(request, 'main/about.html')


def education(request):
    return render(request, 'main/education.html')


def entrant(request):
    return render(request, 'main/entrant.html')


def library(request):
    return render(request, 'main/library.html')


def science(request):
    return render(request, 'main/science.html')


def students(request):
    return render(request, 'main/students.html')


def additional_education(request):
    return render(request, 'main/additional_education.html')


def history(request):
    return render(request, 'main/history.html')
