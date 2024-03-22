from django.shortcuts import render


# Create your views here.

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
