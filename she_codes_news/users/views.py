from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views import generic
from django.views.generic.list import ListView
from .models import CustomUser
from .forms import CustomUserCreationForm


class CreateAccountView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'users/createAccount.html'


class AccountInformationView(ListView):
    model = CustomUser
    template_name = 'users/accountInformation.html'
    #context_object_name = 'user'
