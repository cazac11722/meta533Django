from django.urls import path
from .views import RegisterView, LoginView, UserListView, UserView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),  # 회원가입
    path('login/', LoginView.as_view(), name='login'),           # 로그인
    path('users/', UserListView.as_view(), name='user-list'),    # 모든 회원 정보
    path('users/<int:user>/', UserView.as_view(), name='user-detail'),    # 회원 정보
]
