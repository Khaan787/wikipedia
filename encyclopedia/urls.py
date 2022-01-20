from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:url>", views.entry, name="entry"),
    path("search/", views.search, name="search"),
    path("create/", views.create_page, name="create_page"),
    path("newpage/", views.new_page, name="new_page"),
    path("edit/", views.edit_page, name="edit_page")
]
