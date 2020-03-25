from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.templatetags.static import static

from .models import *
from .serializers import *
import urllib
import os

class DrinksListView(APIView):
    serializer_class = DrinkSerializer
    def get(self,request):
        print("getting all drinks %s"%request.__dict__)
        data = Drink.objects.all()
        base_url =  "{0}://{1}{2}".format(request.scheme, request.get_host(), request.path)
        for d in data:
            d.image = urllib.parse.urljoin(base_url, d.image)
        serialized = DrinkSerializer(data, many=True).data
        return Response(serialized, status=status.HTTP_200_OK)


class AddDrinkView(APIView):
    def post(self, request):
        data = request.data
        print(data)
        drink_type = DrinkType.objects.get(title=data.get('drink_type'))
        name = data.get('drink')
        image = static(os.path.join('brewery', data.get('drink_type'), name) + '.jpg')
        print(drink_type, name, image)
        drink = Drink(name=name, image=image)
        drink.save()
        drink.drink_type.add(drink_type)
        return Response(data, status=status.HTTP_200_OK)
