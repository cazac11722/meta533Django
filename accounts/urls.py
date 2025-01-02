from django.urls import path
from .views import RegisterView, LoginView, UserListView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),  # 회원가입
    path('login/', LoginView.as_view(), name='login'),           # 로그인
    path('users/', UserListView.as_view(), name='user-list'),    # 모든 회원 정보
]
