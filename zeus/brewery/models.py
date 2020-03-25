from django.db import models

# Create your models here.
class DrinkType(models.Model):

    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated = models.DateTimeField(auto_now=True, blank=True, null=True)

    title = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.title or ''

class Drink(models.Model):

    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated = models.DateTimeField(auto_now=True, blank=True, null=True)

    name = models.CharField(max_length=300, null=True, blank=True)
    image = models.URLField(blank=True, null=True)
    drink_type = models.ManyToManyField(DrinkType, blank=True)

    def __str__(self):
        return self.name or ''