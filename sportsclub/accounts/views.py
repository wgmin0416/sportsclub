from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.conf import settings

User = get_user_model()

signup = CreateView.as_view(
    model=User,
    form_class=UserCreationForm,
    success_url=settings.LOGIN_URL,
    template_name='accounts/signup_form.html'
)