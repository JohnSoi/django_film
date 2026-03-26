from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="blog-home"),
    path("category/", views.categories, name="blog-category"),
    path("category/<int:category_id>/", views.category_view, name="blog-category-view")
]