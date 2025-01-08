from django.contrib import admin
from .models import CustomUser, AdvertisingAgency

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'media_name', 'advertiser_name', 'membership_level', 'get_membership_level_display', 'is_active',)

@admin.register(AdvertisingAgency)
class AdvertisingAgencyAdmin(admin.ModelAdmin):
    list_display = ('agency_name', 'contact_person', 'phone_number', 'user')
