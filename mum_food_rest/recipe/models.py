from django.db import models
from ingredient.models import Ingredient


class Recipe(models.Model):
    owner = models.ForeignKey('auth.User', related_name='snippets', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    description = models.CharField(max_length=1000, blank=True, default='')
    vegan = models.BooleanField(default=False)
    vegetarian = models.BooleanField(default=False)
    likes = models.IntegerField()
    ingredients = models.ForeignKey(Ingredient, null=True, on_delete=models.DO_NOTHING)
    class Meta:
        ordering = ['created']