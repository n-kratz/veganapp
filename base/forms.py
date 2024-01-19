from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import *

class BeanForm(ModelForm):
    class Meta:
        model = Serving
        fields = ['title']
    def __init__(self, *args,**kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].queryset = FoodData.objects.filter(category='Beans')

class BerryForm(ModelForm):
    class Meta:
        model = Serving
        fields = ['title']
    def __init__(self, *args,**kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].queryset = FoodData.objects.filter(category='Berries')

class GreenForm(ModelForm):
    class Meta:
        model = Serving
        fields = ['title']
    def __init__(self, *args,**kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].queryset = FoodData.objects.filter(category='Greens')

class NutForm(ModelForm):
    class Meta:
        model = Serving
        fields = ['title']
    def __init__(self, *args,**kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].queryset = FoodData.objects.filter(category='Nuts')

class FlaxForm(ModelForm):
    class Meta:
        model = Serving
        fields = ['title']
    def __init__(self, *args,**kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].queryset = FoodData.objects.filter(category='Flax')

class CVeggiesForm(ModelForm):
    class Meta:
        model = Serving
        fields = ['title']
    def __init__(self, *args,**kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].queryset = FoodData.objects.filter(category='Cruciferous Veggies')

class VeggiesForm(ModelForm):
    class Meta:
        model = Serving
        fields = ['title']
    def __init__(self, *args,**kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].queryset = FoodData.objects.filter(category='Veggies')

class FruitForm(ModelForm):
    class Meta:
        model = Serving
        fields = ['title']
    def __init__(self, *args,**kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].queryset = FoodData.objects.filter(category='Fruits')

class HerbForm(ModelForm):
    class Meta:
        model = Serving
        fields = ['title']
    def __init__(self, *args,**kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].queryset = FoodData.objects.filter(category='Herbs/Spices')

class GrainForm(ModelForm):
    class Meta:
        model = Serving
        fields = ['title']
    def __init__(self, *args,**kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].queryset = FoodData.objects.filter(category='Grains')

class AddFoodForm(ModelForm):
    class Meta:
        model = FoodData
        fields = '__all__'

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['text']

class AddRecipeForm(ModelForm):
    class Meta:
        model = Recipes
        fields = '__all__'
        exclude = ['author']