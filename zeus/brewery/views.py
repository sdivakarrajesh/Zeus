from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

class TopDrinksListView(APIView):
    def get(self,request):
        print("getting")
        data = "It works!"
        return Response(data, status=status.HTTP_200_OK)