from .models import *
from rest_framework import serializers
from django.conf import settings
import os

class DrinkSerializer(serializers.ModelSerializer):
    drink_type = serializers.SerializerMethodField()

    class Meta:
        model = Drink
        fields = ("name", "image", "drink_type")

    def get_drink_type(self,obj):
        drink_types = obj.drink_type.values_list('title', flat=True)
        return ", ".join(drink_types)

        
