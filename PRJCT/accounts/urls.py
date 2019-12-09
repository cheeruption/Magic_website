from django.urls import path
from accounts.views import account_login
from accounts.views import SignUpView
# from .views import account_login


app_name = 'accounts'


urlpatterns = [
    path('', account_login, name='login'),
    path('signup/', SignUpView.as_view(), name='register')   
]
