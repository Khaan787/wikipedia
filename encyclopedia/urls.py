from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:entry>", views.entry, name="entry"),
    path("search/", views.search, name="search"),
    path("create/", views.create_page, name="create_page"),
    path("edit/<str:that_entry>", views.edit_page, name="edit_page"),
    path("random/", views.random_page, name="random_page"),
]
