from .views import *
from django.conf.urls import url

urlpatterns = [
    url(r'^test', TopDrinksListView.as_view()),
]
