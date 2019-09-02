from django.contrib import admin

# Register your models here.
from django.contrib import admin
from ingredient.models import Ingredient

class IngredientAdmin(admin.ModelAdmin):
    pass
admin.site.register(Ingredient, IngredientAdmin)