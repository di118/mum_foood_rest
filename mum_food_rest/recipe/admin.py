from django.contrib import admin

# Register your models here.
from django.contrib import admin
from recipe.models import Recipe, Ingredient

class RecipeAdmin(admin.ModelAdmin):
    pass

class IngredientAdmin(admin.ModelAdmin):
    pass

admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Ingredient, IngredientAdmin)