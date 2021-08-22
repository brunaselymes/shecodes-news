from django.urls import path
from .views import CreateAccountView, AccountInformationView

app_name = 'users'

urlpatterns = [
    path('create-account/', CreateAccountView.as_view(),
         name='createAccount'),
    path('account-information/', AccountInformationView.as_view(),
         name='accountInformation'), ]
