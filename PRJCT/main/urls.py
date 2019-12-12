from django.contrib import admin
from django.urls import path
from main.views import main, about, search_view, confirm_view


app_name = 'main'

urlpatterns = [
    path('', main, name = 'main'),
    path('about/', about, name = 'about'),
    path('search/', search_view, name = 'search'),
    path('confirm/',confirm_view, name = 'confirm')
]
