from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    # 추가 필드
    media_name = models.CharField(max_length=255, null=True, blank=True, verbose_name="매체명")
    advertiser_name = models.CharField(max_length=255, null=True, blank=True, verbose_name="광고주명")
    contact_person = models.CharField(max_length=255, null=True, blank=True, verbose_name="담당자")
    phone_number = models.CharField(max_length=20, null=True, blank=True, verbose_name="전화번호")
    
    MEMBERSHIP_LEVELS = [
        (1, 'Bronze'),
        (2, 'Silver'),
        (3, 'Gold'),
        (4, 'Platinum'),
    ]
    membership_level = models.IntegerField(
        choices=MEMBERSHIP_LEVELS,
        default=1,
        verbose_name="회원 등급"
    )
    is_active = models.CharField(max_length=255, null=True, default=True, verbose_name="진행 여부")

    def get_membership_level_display(self):
        """회원 등급 숫자를 문자열로 반환"""
        return dict(self.MEMBERSHIP_LEVELS).get(self.membership_level, "Unknown")

    def __str__(self):
        return self.username


class AdvertisingAgency(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="advertising_agencies", verbose_name="회원")
    agency_name = models.CharField(max_length=255, verbose_name="광고대행사명")
    contact_person = models.CharField(max_length=255, verbose_name="담당자")
    phone_number = models.CharField(max_length=20, verbose_name="전화번호")
    email = models.EmailField(verbose_name="이메일")
    memo = models.TextField(null=True, blank=True, verbose_name="메모")

    def __str__(self):
        return self.agency_name
