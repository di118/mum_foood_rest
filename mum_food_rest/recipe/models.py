from django.db import models
from django.db.models import Q

class RecipeManager(models.Manager):
    def search(self, query=None):
        qs = self.get_queryset()
        if query is not None:
            or_lookup = (Q(title__icontains=query) |
                         Q(ingredients__name__icontains=query)|
                         Q(likes__icontains=query)|
                         Q(vegan__icontains=query)
                        )
            qs = qs.filter(or_lookup).distinct() # distinct() is often necessary with Q lookups
        return qs

class Ingredient(models.Model):
    name = models.CharField(max_length=255, unique=True, primary_key=True)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return u"%s" % (self.name)


class Recipe(models.Model):
    owner = models.ForeignKey('auth.User', related_name='recipe', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    description = models.CharField(max_length=1000, blank=True, default='')
    vegan = models.BooleanField(default=False)
    vegetarian = models.BooleanField(default=False)
    likes = models.IntegerField(default=0)
    ingredients = models.ManyToManyField(Ingredient)

    objects = RecipeManager()

    class Meta:

        ordering = ['likes']