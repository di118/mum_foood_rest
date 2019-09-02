from django.urls import path
from recipe import views
from rest_framework.urlpatterns import format_suffix_patterns
# from recipe.views import RecipeViewSet, UserViewSet, api_root
from rest_framework import renderers

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from recipe import views

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'recipe', views.RecipeViewSet)
router.register(r'users', views.UserViewSet)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]

# recipe_list = RecipeViewSet.as_view({
#     'get': 'list',
#     'post': 'create'
# })
# recipe_detail = RecipeViewSet.as_view({
#     'get': 'retrieve',
#     'put': 'update',
#     'patch': 'partial_update',
#     'delete': 'destroy'
# })
# user_list = UserViewSet.as_view({
#     'get': 'list'
# })
# user_detail = UserViewSet.as_view({
#     'get': 'retrieve'
# })
#
# urlpatterns = format_suffix_patterns([
#     path('', api_root),
#     path('recipe/', recipe_list, name='recipe-list'),
#     path('recipe/<int:pk>/', recipe_detail, name='recipe-detail'),
#     path('users/', user_list, name='user-list'),
#     path('users/<int:pk>/', user_detail, name='user-detail')
# ])