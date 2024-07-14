from rest_framework import serializers

class RecipeSerializer(serializers.Serializers):

    id = serializers.IntegerField()
    title = serializers.CharField(max_characters=255)
    ingredients = serializers.ListField(child = serializers.CharField(max_characters=100))
    cuisine = serializers.CharField(max_characters=255)
    instructions = serializers.ListField(child = serializers.CharField())
    ratings = serializers.IntegerField()