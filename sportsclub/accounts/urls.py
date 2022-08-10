from django.contrib.auth.views import LoginView
from django.urls import path

urlpatterns = [
    # 회원가입
    # path('signup/', UserC)
    # 로그인
    path('login/', LoginView.as_view(template_name='accounts/login_form.html'), name='login')
]