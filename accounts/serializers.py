from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id', 
            'username', 
            'email', 
            'password', 
            'first_name', 
            'last_name',
            'media_name',
            'advertiser_name',
            'contact_person',
            'phone_number',
            'membership_level',
            'is_active',
        ]
        extra_kwargs = {
            'password': {'write_only': True},  # 비밀번호는 쓰기 전용으로 설정
        }

    def create(self, validated_data):
        """
        사용자 생성. 비밀번호는 자동 암호화됨.
        """
        user = User.objects.create_user(**validated_data)
        return user


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        """
        토큰 생성 및 사용자 정보 추가.
        """
        data = super().validate(attrs)

        # 사용자 추가 정보 반환
        data['user_id'] = self.user.id
        data['username'] = self.user.username
        data['email'] = self.user.email
        data['membership_level'] = self.user.membership_level
        data['media_name'] = self.user.media_name
        data['advertiser_name'] = self.user.advertiser_name

        return data
