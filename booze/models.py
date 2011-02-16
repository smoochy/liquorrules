from django.db import models

class DrinkLink(models.Model):
    name = models.CharField(max_length=100)
    href = models.CharField(max_length=200)
    scraped = models.BooleanField(default=False)

class Cocktail(models.Model):
    name = models.CharField(max_length=100)
    summary = models.TextField()
    instructions = models.TextField()

class Ingredient(models.Model):
    amount = models.CharField(max_length=50)
    name = models.CharField(max_length=100)
    cocktail = models.ForeignKey('booze.Cocktail')
