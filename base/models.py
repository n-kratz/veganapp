from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from django.core.validators import MaxValueValidator, MinValueValidator

class FoodData(models.Model):
    title = models.CharField(max_length = 20)

    CATEGORY = (
        ('Beans', 'Beans'),
        ('Greens', 'Greens'),
        ('Berries', 'Berries'),
        ('Nuts', 'Nuts'),
        ('Flax', 'Flax'),
        ('Cruciferous Veggies', 'Cruciferous Veggies'),
        ('Veggies', 'Veggies'),
        ('Fruits', 'Fruits'),
        ('Herbs/Spices', 'Herbs/Spices'),
        ('Grains', 'Grains')
    )
    
    category = models.CharField(max_length = 20, choices=CATEGORY, default='Beans')
    calories = models.IntegerField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    calperlb = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.title

class Serving(models.Model):
    title = models.ForeignKey(FoodData, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class InputData(models.Model):
    date = models.DateTimeField()
    dailyCost = models.DecimalField(max_digits=5, decimal_places=2)
    dailyCalories = models.IntegerField()
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)

class Rating(models.Model):
    recipe_id = models.IntegerField(null=True, blank=True)
    score = models.IntegerField(default=0,
        validators=[
            MaxValueValidator(5),
            MinValueValidator(0),
        ]
    )
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return str(self.score)

class Comment(models.Model):
    rating = models.ForeignKey(Rating, null=True, blank=True, on_delete=models.CASCADE)
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    text = models.TextField(max_length=250)
    date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return str(self.id)

class Recipes(models.Model):
    title = models.CharField(max_length = 100)
    description = models.CharField(max_length = 200)
    ingredients = RichTextField(max_length=500)
    instructions = RichTextField(max_length=500)
    author = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    pic = models.ImageField()

    def __str__(self):
        return self.title

    def avg_rating(self):
        if Rating.objects.filter(recipe_id=self.id).aggregate(models.Avg("score"))['score__avg'] == None:
            return 0
        else:
            return round(Rating.objects.filter(recipe_id=self.id).aggregate(models.Avg("score"))['score__avg'], 2)
    