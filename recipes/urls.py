from django.urls import path
from .views import RecipeList, RecipeDetail

urlpatterns = [
    path('', RecipeList.as_view(), name='recipe-list'),
    path('<int:id>', RecipeDetail.as_view(), name='recipe-detail')
]
