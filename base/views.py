from django.shortcuts import render, redirect
from django.forms import formset_factory
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.decorators import login_required

import datetime

from .models import *
from .forms import *
from .filters import *
from .decorators import unauthenticated_user

@unauthenticated_user
def register(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account created for ' + user)
            return redirect('login')

    context = {'form': form}
    return render(request, 'base/register.html', context)

@unauthenticated_user
def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username OR password is incorrect')
            return render(request, 'base/login.html')

    return render(request, 'base/login.html')

def logoutUser(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def dozenList(request):
    beanformset = formset_factory(BeanForm, extra=3)
    berryformset = formset_factory(BerryForm, extra=1)
    greenformset = formset_factory(GreenForm, extra=2)
    nutformset = formset_factory(NutForm, extra=1)
    flaxformset = formset_factory(FlaxForm, extra=1)
    cvegformset = formset_factory(CVeggiesForm, extra=1)
    vegformset = formset_factory(VeggiesForm, extra=2)
    fruitformset = formset_factory(FruitForm, extra=3)
    herbformset = formset_factory(HerbForm, extra=1)
    grainformset = formset_factory(GrainForm, extra=3)

    formset=beanformset(prefix='bean')
    berry_formset = berryformset(prefix='berry')
    green_formset = greenformset(prefix='green')
    nut_formset = nutformset(prefix='nut')
    flax_formset = flaxformset(prefix='flax')
    cveg_formset = cvegformset(prefix='cveg')
    veg_formset = vegformset(prefix='veg')
    fruit_formset = fruitformset(prefix='fruit')
    herb_formset = herbformset(prefix='herb')
    grain_formset = grainformset(prefix='grain')

    if request.method == 'POST':
        print(request.user)
        food_list = [request.POST['bean-0-title'], request.POST['bean-1-title'], request.POST['bean-2-title'],
        request.POST['berry-0-title'],
        request.POST['green-0-title'], request.POST['green-1-title'],
        request.POST['nut-0-title'], 
        request.POST['flax-0-title'],
        request.POST['cveg-0-title'],
        request.POST['veg-0-title'], request.POST['veg-1-title'],
        request.POST['fruit-0-title'], request.POST['fruit-1-title'], request.POST['fruit-2-title'],
        request.POST['herb-0-title'],
        request.POST['grain-0-title'], request.POST['grain-1-title'], request.POST['grain-2-title'],
        ]

        sum_cost = 0
        sum_calories = 0
        for food in food_list:
            name = FoodData.objects.get(id=food)
            sum_cost += name.price
            sum_calories += name.calories

        InputData.objects.create(
            date = datetime.datetime.now(),
            dailyCost = sum_cost,
            dailyCalories = sum_calories,
            user = request.user
        )
        
        inputs = InputData.objects.filter(user=request.user)

        context = {
            'inputs': inputs
            }

        return render(request, 'base/enterserving.html', context)

    context={
        'formset': formset,
        'berry_formset': berry_formset,
        'green_formset': green_formset,
        'nut_formset': nut_formset,
        'flax_formset': flax_formset,
        'cveg_formset': cveg_formset,
        'veg_formset': veg_formset,
        'fruit_formset': fruit_formset,
        'herb_formset': herb_formset,
        'grain_formset': grain_formset
    }
    
    return render(request, 'base/dozenlist.html', context)

@login_required(login_url='login')
def enterServing(request):
    inputs = InputData.objects.filter(user=request.user)

    context = {
        'inputs': inputs
        }
    return render(request, 'base/enterserving.html', context)

@login_required(login_url='login')
def searchFoods(request):
    foods = FoodData.objects.all().order_by('calperlb')

    myFilter = FoodFilter(request.GET, queryset=foods)
    foods=myFilter.qs

    context = {
        'foods': foods,
        'myFilter': myFilter, }
    return render(request, 'base/searchfoods.html', context)

@login_required(login_url='login')
def addFood(request):
    form = AddFoodForm()
    if request.method == 'POST':
        form = AddFoodForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('search')

    context = {'form': form}
    return render(request, 'base/addfood.html', context)

@login_required(login_url='login')
def updateFood(request, pk):
    food = FoodData.objects.get(id=pk)
    
    form = AddFoodForm(instance=food)
    if request.method == 'POST':
        form = AddFoodForm(request.POST, instance=food)
        if form.is_valid():
            form.save()
            return redirect('search')

    context = {'form': form}
    return render(request, 'base/addfood.html', context)

@login_required(login_url='login')
def deleteFood(request, pk):
    food = FoodData.objects.get(id=pk)
    if request.method == 'POST':
        food.delete()
        return redirect('search')

    context = {'food': food}
    return render(request, 'base/delete.html', context)

@login_required(login_url='login')
def recipes(request):
    recipes = Recipes.objects.all()

    myFilter = RecipeFilter(request.GET, queryset=recipes)
    recipes=myFilter.qs

    context = {
        'recipes': recipes,
        'myFilter': myFilter, }
    return render(request, 'base/recipes.html', context)

@login_required(login_url='login')
def view_recipe(request, pk):
    recipe = Recipes.objects.get(id=pk)
    comments = Comment.objects.filter(rating__recipe_id=pk)

    form = CommentForm()
    if request.method == 'POST':
        rating = Rating.objects.filter(user=request.user).last()
        Comment.objects.create(
            text = request.POST['text'],
            rating = rating,
            date = datetime.datetime.now(),
            user = request.user,
        )

    context = {
        'recipe': recipe,
        'form': form,
        'comments': comments,
        }
    return render(request, 'base/view_recipe.html', context)

@login_required(login_url='login')
def star_rate(request):
    if request.method == 'POST':
        el_id = request.POST['el_id']
        val = request.POST['val']
        print(val)
        Rating.objects.create(
            recipe_id = el_id,
            score = val,
            user = request.user,
            date = datetime.datetime.now(),
        )
        return JsonResponse({'success':'true', 'score': val}, safe=False)
    return JsonResponse({'success':'false'})

@login_required(login_url='login')
def addRecipe(request):
    form = AddRecipeForm()
    if request.method == 'POST':
        form = AddRecipeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            recipe = Recipes.objects.last()
            recipe.author = request.user
            recipe.save()
            return redirect('recipes')

    context = {'form': form}
    return render(request, 'base/add_recipe.html', context)