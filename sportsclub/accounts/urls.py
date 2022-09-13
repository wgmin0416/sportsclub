from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from .views import AccountsCreateView

urlpatterns = [
    # 회원가입
    path('signup/', AccountsCreateView.as_view(), name='signup'),
    # 로그인
    path('login/', LoginView.as_view(template_name='accounts/login_form.html'), name='login'),
    # 로그아웃
    path('logout/', LogoutView.as_view(), name='logout'),

    # 홈 화면
    path('/', name='home'),
]