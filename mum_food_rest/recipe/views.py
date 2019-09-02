from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from mum_food_rest.serializers import UserSerializer, GroupSerializer
from rest_framework.parsers import JSONParser
from recipe.models import Recipe
from rest_framework import status
from rest_framework.decorators import api_view
from recipe.serializers import RecipeSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import mixins
from rest_framework import generics
from django.contrib.auth.models import User
from recipe.serializers import UserSerializer
from rest_framework import permissions
from recipe.permissions import IsOwnerOrReadOnly
from rest_framework import viewsets
from rest_framework.decorators import action


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class RecipeViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.


    """
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]


    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
# class UserDetail(generics.RetrieveAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#
# class UserViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows users to be viewed or edited.
#     """
#     queryset = User.objects.all().order_by('-date_joined')
#     serializer_class = UserSerializer


# class RecipeList(generics.ListCreateAPIView):
#     queryset = Recipe.objects.all()
#     serializer_class = RecipeSerializer
#
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly]
#
#     def perform_create(self, serializer):
#         serializer.save(owner=self.request.user)
#
# class RecipeDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Recipe.objects.all()
#     serializer_class = RecipeSerializer
#
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly,
#                           IsOwnerOrReadOnly]
# # @api_view(['GET', 'POST'])
# # def recipe_list(request, format=None):
# #     """
# #     List all code snippets, or create a new snippet.
# #     """
# #     if request.method == 'GET':
# #         recipe = Recipe.objects.all()
# #         serializer = RecipeSerializer(recipe, many=True)
# #         return Response(serializer.data)
# #
# #     elif request.method == 'POST':
# #         serializer = RecipeSerializer(data=request.data)
# #         if serializer.is_valid():
# #             serializer.save()
# #             return Response(serializer.data, status=status.HTTP_201_CREATED)
# #         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# # class RecipeList(APIView):
# #     """
# #     List all snippets, or create a new snippet.
# #     """
# #     def get(self, request, format=None):
# #         recipe = Recipe.objects.all()
# #         serializer = RecipeSerializer(recipe, many=True)
# #         return Response(serializer.data)
# #
# #     def post(self, request, format=None):
# #         serializer = RecipeSerializer(data=request.data)
# #         if serializer.is_valid():
# #             serializer.save()
# #             return Response(serializer.data, status=status.HTTP_201_CREATED)
# #         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
# # @api_view(['GET', 'PUT', 'DELETE'])
# # def recipe_detail(request, pk, format=None):
# #     """
# #     Retrieve, update or delete a code snippet.
# #     """
# #     try:
# #         recipe = Recipe.objects.get(pk=pk)
# #     except Recipe.DoesNotExist:
# #         return Response(status=status.HTTP_404_NOT_FOUND)
# #
# #     if request.method == 'GET':
# #         serializer = RecipeSerializer(recipe)
# #         return Response(serializer.data)
# #
# #     elif request.method == 'PUT':
# #         data = JSONParser().parse(request)
# #         serializer = RecipeSerializer(recipe, data=data)
# #         if serializer.is_valid():
# #             serializer.save()
# #             return Response(serializer.data)
# #         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# #
# #     elif request.method == 'DELETE':
# #         recipe.delete()
# #         return Response(status=status.HTTP_204_NO_CONTENT)
#
# # class RecipeDetail(APIView):
# #     """
# #     Retrieve, update or delete a snippet instance.
# #     """
# #     def get_object(self, pk):
# #         try:
# #             return Recipe.objects.get(pk=pk)
# #         except Recipe.DoesNotExist:
# #             raise Http404
# #
# #     def get(self, request, pk, format=None):
# #         recipe = self.get_object(pk)
# #         serializer = RecipeSerializer(recipe)
# #         return Response(serializer.data)
# #
# #     def put(self, request, pk, format=None):
# #         recipe = self.get_object(pk)
# #         serializer = RecipeSerializer(recipe, data=request.data)
# #         if serializer.is_valid():
# #             serializer.save()
# #             return Response(serializer.data)
# #         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# #
# #     def delete(self, request, pk, format=None):
# #         recipe = self.get_object(pk)
# #         recipe.delete()
# #         return Response(status=status.HTTP_204_NO_CONTENT)