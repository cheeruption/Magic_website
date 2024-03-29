from django.shortcuts import render, redirect
from .forms import AccountUserForm
from django.contrib.auth import authenticate, login
from django.urls import reverse_lazy

# Create your views here.

def account_login(request):

	success_url = reverse_lazy('main:main')
	form = AccountUserForm()

	if request.method == 'POST':
		form = AccountUserForm(data=request.POST)

		if form.is_valid():
			usr = form.cleaned_data.get('username') #из объекта формы достанем чистый словарь, оттуда юзернейм
			pwd = form.cleaned_data.get('password')
			user = authenticate(
				username=usr,
				password=pwd,
			)

			if user and user.is_active:
				login(request, user)
				return redirect(success_url)

	return render(request, 'accounts/login.html', {'form':form})