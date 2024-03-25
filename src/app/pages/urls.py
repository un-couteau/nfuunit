from django.urls import path
from . import views

urlpatterns = [
    # path("", views.main, name="main"),
    path("about/", views.about, name="about"),
    path("education/", views.education, name="education"),
    path("entrant/", views.entrant, name="entrant"),
    path("library/", views.entrant, name="library"),
    path("science/", views.science, name="science"),
    path("students/", views.students, name="students"),
    path("additional_education/", views.students, name="additional_education"),
    path("history/", views.history, name="history"),
    path("", views.index, name="index")
]
