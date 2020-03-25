from .views import *
from django.conf.urls import url

urlpatterns = [
    url(r'^drinks/all', DrinksListView.as_view()),
    url(r'^drink/add/', AddDrinkView.as_view()),
]
