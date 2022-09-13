from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.conf import settings
from django.urls import reverse_lazy

User = get_user_model()
class AccountsCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url: reverse_lazy('accounts:login')
    template_name = 'signup_form.html'