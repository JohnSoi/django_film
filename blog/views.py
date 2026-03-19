from django.shortcuts import render

from blog.models import Film


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

def about(request):
    return render(
        request,
        "blog/about.html",
        {"title": "О нас"}
    )
