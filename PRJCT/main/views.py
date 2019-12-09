from django.template.loader import render_to_string
from django.http import HttpResponse
from django.shortcuts import render
from .forms import SearchForm
import requests
import re



# Create your views here.
def main(request):

    return render(request, 'main/index.html')


def about(request):

    return render(request,'main/about.html')


def search(request):
    form = SearchForm() #вывести на экран форму так как она описана в .forms
    context = 'nothing_here yet... TRY TO INPUT SOMETHING!' #заглушка для контекста

    if request.method == "POST": #если запрос к странице содержит ПОСТ запрос - идем по данному пути
        form = SearchForm(request.POST) #вытаскиваем объект формы
        if form.is_valid():
            context = {'card':form.cleaned_data.get('cardname')}
    return render(request, "main/prices.html", {'card':context, 'form':form})