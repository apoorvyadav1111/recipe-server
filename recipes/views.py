from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import render
from pathlib import Path
from rest_framework import status
import json
# Create your views here.
DATA_FILE = Path(__file__).resolve().parent / "data/recipes.json"

class RecipeList(APIView):
    def get(self, request):
        with open(DATA_FILE,'r') as f:
            recipes = json.load(f)
        resp = []
        for recipe in recipes:
            resp.append({
                'id':recipe['id'],
                'title':recipe['title'],
                'rating':recipe['rating'],
                'cuisine':recipe['cuisine']
            })
        return Response(resp)
    
class RecipeDetail(APIView):
    def get(self,request, id):
        with open(DATA_FILE,'r') as f:
            recipes = json.load(f)
        
        for recipe in recipes:
            if recipe['id'] == id:
                return Response(recipe)

        return Response(status=status.HTTP_404_NOT_FOUND)
                