from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import status
from rest_framework import serializers
from .serializers import CustomTokenObtainPairSerializer, UserSerializer
from .models import AdvertisingAgency
from django.contrib.auth import get_user_model

User = get_user_model()

class AdvertisingAgencySerializer(serializers.ModelSerializer):
    """
    광고대행사 정보 시리얼라이저
    """
    class Meta:
        model = AdvertisingAgency
        fields = ['id', 'agency_name', 'contact_person', 'phone_number', 'email', 'memo']


class ExtendedUserSerializer(serializers.ModelSerializer):
    """
    사용자 정보 시리얼라이저 (광고대행사 정보 포함)
    """
    advertising_agencies = AdvertisingAgencySerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'email',
            'first_name',
            'last_name',
            'media_name',
            'advertiser_name',
            'contact_person',
            'phone_number',
            'membership_level',
            'advertising_agencies',
            'is_active',
        ]


class RegisterView(APIView):
    """
    회원가입 API
    """
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            refresh = RefreshToken.for_user(user)
            return Response({
                "message": "회원가입 성공",
                "user": {
                    "id": user.id,
                    "username": user.username,
                    "email": user.email,
                },
                "tokens": {
                    "refresh": str(refresh),
                    "access": str(refresh.access_token),
                }
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(TokenObtainPairView):
    """
    로그인 API
    """
    serializer_class = CustomTokenObtainPairSerializer


class UserListView(APIView):
    """
    모든 회원 정보 보기 API (광고대행사 정보 포함)
    """
    permission_classes = [AllowAny]

    def get(self, request):
        users = User.objects.all()
        serializer = ExtendedUserSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
