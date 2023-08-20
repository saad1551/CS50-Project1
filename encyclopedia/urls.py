from django.urls import path

from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>", views.entry, name="entry"),
    path("wikisearch", views.search, name="search"),
    path("newpage", views.new, name="new"),
    path("editpage", views.edit, name="edit"),
    path("randompage", views.random, name="random")
]
