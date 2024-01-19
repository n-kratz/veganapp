from django.urls import path
from . import views

urlpatterns = [
    path("register/", views.register, name='register'),
    path("login/", views.loginPage, name='login'),
    path("logout/", views.logoutUser, name='logout'),
    
    path("", views.dozenList, name="home"),
    path("serving/", views.enterServing, name="serving"),
    path("search/", views.searchFoods, name="search"),
    path("add/", views.addFood, name="add_food"),
    path("update/<str:pk>/", views.updateFood, name="update_food"),
    path("delete/<str:pk>/", views.deleteFood, name="delete_food"),
    path("recipes/", views.recipes, name="recipes"),
    path("view_recipe/<str:pk>/", views.view_recipe, name="view_recipe"),

    path('rate/', views.star_rate, name='star_rate'),
    path('add_recipe/', views.addRecipe, name='add_recipe'),
]