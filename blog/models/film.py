from django.db import models

from .category import Category


class Film(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    poster = models.TextField(null=True)
    category = models.ForeignKey(
        Category, null=True, on_delete=models.SET_NULL
    )

    def __str__(self) -> str:
        return self.name