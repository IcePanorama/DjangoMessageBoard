from django.urls import path

from . import views

app_name = "board"

urlpatterns = [
    path("", views.index, name="index"),
    path("thread/<int:thread_id>/", views.thread, name="thread"),
    path("archive/", views.archive, name="archive"),
]
