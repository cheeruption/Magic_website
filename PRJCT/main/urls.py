from django.contrib import admin
from django.urls import path
from main.views import main, about, search


app_name = 'main'

urlpatterns = [
    path('', main, name = 'main'),
    path('about/', about, name = 'about'),
    # path('search/', search, name='search')
]
