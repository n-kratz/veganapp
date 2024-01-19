from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(FoodData)
admin.site.register(InputData)
admin.site.register(Recipes)
admin.site.register(Rating)
admin.site.register(Comment)