from django.contrib import admin
from .models import LandingPage, Visit, VisitDetail, Application, ApplicationDetail

@admin.register(LandingPage)
class LandingPageAdmin(admin.ModelAdmin):
    list_display = ("title", "url", "ad_platform", "start_date", "end_date", "ad_cost")
    search_fields = ("title", "url", "ad_platform")

@admin.register(Visit)
class VisitAdmin(admin.ModelAdmin):
    list_display = ("landing_page", "visit_count", "visit_cost", "bounce_count")
    list_filter = ("landing_page",)

@admin.register(VisitDetail)
class VisitDetailAdmin(admin.ModelAdmin):
    list_display = ("visit", "device_type", "ip_address", "session_start", "session_end", "exit_y_coordinate")
    list_filter = ("device_type",)

@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ("landing_page", "application_count", "application_cost")
    list_filter = ("landing_page",)

@admin.register(ApplicationDetail)
class ApplicationDetailAdmin(admin.ModelAdmin):
    list_display = ("application", "name", "contact", "consultation_request_time", "consultation_result", "application_date")
    list_filter = ("consultation_result",)
    search_fields = ("name", "contact")
