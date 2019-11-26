from django.template.loader import render_to_string
from django.http import HttpResponse
from django.shortcuts import render



# Create your views here.
def main(request):

    return render(request, 'main/index.html')


def about(request):

    return render(request,'main/about.html')