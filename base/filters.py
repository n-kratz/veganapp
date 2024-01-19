import django_filters
from django_filters import CharFilter

from .models import *

class FoodFilter(django_filters.FilterSet):
    title = CharFilter(field_name='title', lookup_expr='icontains')
    class Meta:
        model = FoodData
        fields = ['title', 'category']

class RecipeFilter(django_filters.FilterSet):
    ingredients = CharFilter(field_name='ingredients', lookup_expr='icontains')
    title = CharFilter(field_name='title', lookup_expr='icontains')
    class Meta:
        model = Recipes
        fields = ['title', 'ingredients', 'author']