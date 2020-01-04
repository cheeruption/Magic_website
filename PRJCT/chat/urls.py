from django.contrib import admin
from django.urls import path
from chat.views import index, room


app_name = 'chat'

urlpatterns = [
    path('', index, name = 'chat'),
    path('<str:room_name>/', room, name='room')
]
