from django.http import HttpResponse
from django.shortcuts import render

from blog.models import Film, Category


# Create your views here.
def home(request):
    return render(
        request,
        "blog/home.html",
        {
            "title": "Все фильмы",
            "films": Film.objects.all()
        }
    )

def categories(request):
    return render(
        request,
        "blog/categories.html",
        {
            "title": "Категории",
            "categories": Category.objects.all()
        }
    )


def category_view(request, category_id):
    category_data = Category.objects.all().get(pk=category_id)
    films = None

    if category_data:
        films = Film.objects.all().filter(category=category_data)

    return render(
        request,
        'blog/film-by-category.html',
        {
            "category": category_data,
            "films": films
        }
    )


