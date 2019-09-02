from django.urls import path
from recipe import views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    path('recipe/', views.recipe_list),
    path('recipe/<int:pk>/', views.recipe_detail),
]
urlpatterns = format_suffix_patterns(urlpatterns)