from django.contrib import admin
from .models import *
# Register your models here.
class DrinkAdmin(admin.ModelAdmin):
    list_display = ("name", "image")

class DrinkTypeAdmin(admin.ModelAdmin):
    list_display = ("title",)

admin.site.register(Drink, DrinkAdmin)
admin.site.register(DrinkType, DrinkTypeAdmin)