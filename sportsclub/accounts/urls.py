from django.contrib.auth.views import LoginView
from django.views.generic import CreateView
from django.urls import path
from .views import signup

urlpatterns = [
    # 회원가입
    path('signup/', CreateView.as_view(template_name='accounts/signup_form.html'), name='signup'),
    # 로그인
    path('signin/', LoginView.as_view(template_name='accounts/signin_form.html'), name='signin')
]