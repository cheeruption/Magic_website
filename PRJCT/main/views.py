from django.template.loader import render_to_string
from django.http import HttpResponse
from django.shortcuts import render
from .forms import SearchForm
import requests
import re
import telebot
from telebot.types import Message
import shutil
from telebot import apihelper
from time import sleep
sleep(0.05)


# Create your views here.
def main(request):

    return render(request, 'main/index.html')


def about(request):

    return render(request,'main/about.html')

def search_view(request):

    form = SearchForm() #вывести на экран форму так как она описана в .forms
    context = 'nothing_here yet... TRY TO INPUT SOMETHING!' #заглушка для контекста

    if request.method == "POST": #если запрос к странице содержит ПОСТ запрос - идем по данному пути
        form = SearchForm(request.POST) #вытаскиваем объект формы
        if form.is_valid():
            context = form.cleaned_data.get('cardname').replace('','+')
            search_upd = f'https://api.scryfall.com/cards/named?fuzzy={context}'
            r = requests.get(search_upd)
            api_respond = r.json()
            context = api_respond.get('name')

    return render(request, "main/prices.html", {'card':context, 'form':form})

def confirm_view(request):
    verdict = 'Successfull'
    http_proxy  = "socks5://retterproxy:Gorikbest123@kemper1t.ru:1081"
    https_proxy = "socks5://retterproxy:Gorikbest123@kemper1t.ru:1081"
    ftp_proxy   = "socks5://retterproxy:Gorikbest123@kemper1t.ru:1081"

    proxyDict = { 
                  "http"  : http_proxy, 
                  "https" : https_proxy, 
                  "ftp"   : ftp_proxy
                }

    BASE_URL = 'https://api.telegram.org/bot735263028:AAFvj0eR3w-bp13YNue_pnswn22HADoEN18/'

    r = requests.get(f'{BASE_URL}getMe',proxies=proxyDict)
    r = requests.get(f'{BASE_URL}getUpdates',proxies=proxyDict)

    payload = {}
    payload['chat_id'] = 159195360
    payload['text'] = 'Here comes an ORDER! Say OK'

    print('payload = ', payload)

    # отправляем сообщение по указанному выше chat id для проверки связи
    r = requests.post(f'{BASE_URL}sendMessage',proxies=proxyDict,data=payload)
    sleep(10)
    r = requests.get(f'{BASE_URL}getUpdates',proxies=proxyDict)
    verdict = r[updates][text]


	return render(request,"main/confirm.html", {'verdict':verdict})

# поиск картинки по названию + перевод карты с ру на англ
# SEARCHCARD = 'Fanat Fire'.replace(' ','+')
# SEARCHCARD = input('what card? ').replace(' ','+')
# search_upd = f'https://api.scryfall.com/cards/named?fuzzy={SEARCHCARD}'
# r = requests.get(search_upd)
# api_respond = r.json()


# print(api_respond)

# print(api_respond['image_uris'])

# request_image = api_respond['image_uris']['normal']
# print(request_image)
# r = requests.get(request_image, stream = True)
# if r.status_code == 200:
#     with open('test.jpg', 'wb') as f:
#         r.raw.decode_content = True
#         shutil.copyfileobj(r.raw, f)
# else:
#     print('smth went wrong')