from django import forms

'''
Данный файл отвечает за страницу на которой пользователь может заполнить данные о своём профиле

'''

class AccountUserForm(forms.Form):
    username = forms.CharField(
        label='Login', max_length=150,
        widget=forms.widgets.TextInput(
            attrs={'class': 'field_username'}
        )
    )
    password = forms.CharField(
        max_length=250, 
        widget=forms.widgets.PasswordInput(
            attrs={'class': 'field_password'}
        )
    )
