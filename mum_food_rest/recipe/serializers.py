from rest_framework import serializers
from recipe.models import Recipe

#
# class RecipeSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     title = serializers.CharField(required=False, allow_blank=True, max_length=100)
#     description = serializers.CharField(required=False)
#     vegan = serializers.BooleanField(required=False)
#     vegetarian = serializers.BooleanField(required=False)
#     likes = serializers.IntegerField(required=False)
#     ingredients = serializers.CharField(required=False)
#
#     def create(self, validated_data):
#         """
#         Create and return a new `Recipe` instance, given the validated data.
#         """
#         return Recipe.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         """
#         Update and return an existing `Snippet` instance, given the validated data.
#         """
#         instance.title = validated_data.get('title', instance.title)
#         instance.description = validated_data.get('description', instance.description)
#         instance.vegan = validated_data.get('vegan', instance.vegan)
#         instance.vegetarian = validated_data.get('vegetarian', instance.vegetarian)
#         instance.likes = validated_data.get('likes', instance.likes)
#         instance.ingredients = validated_data.get('ingredients', instance.ingredients)
#         instance.save()
#         return instance

class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = ['id', 'title', 'description', 'vegan', 'vegetarian', 'likes','ingredients']