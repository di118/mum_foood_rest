from django.db import models


class Ingredient(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Recipe(models.Model):
    owner = models.ForeignKey('auth.User', related_name='snippets', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    description = models.CharField(max_length=1000, blank=True, default='')
    vegan = models.BooleanField(default=False)
    vegetarian = models.BooleanField(default=False)
    likes = models.IntegerField()
    ingredients = models.ManyToManyField(Ingredient)
    class Meta:
        ordering = ['created']