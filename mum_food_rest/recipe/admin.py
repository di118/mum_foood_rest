from django.contrib import admin

# Register your models here.
from django.contrib import admin
from recipe.models import Recipe

class RecipeAdmin(admin.ModelAdmin):
    pass
admin.site.register(Recipe, RecipeAdmin)