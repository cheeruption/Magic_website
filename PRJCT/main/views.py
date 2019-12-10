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

def search_view(request):
	return render(request,'main/about.html')
# def search_view(request):
#     form = SearchForm() #вывести на экран форму так как она описана в .forms
#     context = 'nothing_here yet... TRY TO INPUT SOMETHING!' #заглушка для контекста

#     if request.method == "POST": #если запрос к странице содержит ПОСТ запрос - идем по данному пути
#         form = SearchForm(request.POST) #вытаскиваем объект формы
#         if form.is_valid():
#             context = form.cleaned_data.get('cardname').replace('','+')
#             search_upd = f'https://api.scryfall.com/cards/named?fuzzy={context}'
#             r = requests.get(search_upd)
#             api_respond = r.json()
#             context = api_respond.get('name')

#     return render(request, "main/prices.html", {'card':context, 'form':form})

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