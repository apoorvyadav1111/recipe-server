from django.urls import path
from .views import RecipeList, RecipeDetail

urlpatterns = [
    path('recipes/', RecipeList.as_view(), name='recipe-list'),
    path('recipes/<int:id>', RecipeDetail.as_view(), name='recipe-detail')
]
