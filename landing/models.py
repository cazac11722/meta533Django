from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class LandingPage(models.Model):
    user = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, 
        related_name="landing_pages", 
        help_text="The user who owns this landing page",
        default=1
    )
    title = models.CharField(max_length=255, help_text="Title of the landing page")
    url = models.CharField(max_length=500, help_text="URL of the landing page")
    ad_platform = models.CharField(max_length=255, help_text="Advertising platform associated with the landing page")
    start_date = models.DateField( help_text="Advertisement start date")
    end_date = models.DateField(blank=True, null = True, default=None, help_text="Advertisement end date")
    ad_cost = models.DecimalField(blank=True, null = True, max_digits=10, decimal_places=2, default=0.0, help_text="Total advertisement cost")
    html_content = models.TextField(blank=True, null=True, help_text="HTML content of the landing page")

    def __str__(self):
        return f"{self.title} by {self.user.username}"

class Visit(models.Model):
    landing_page = models.ForeignKey(LandingPage, on_delete=models.CASCADE, related_name="visits", help_text="Related landing page")
    visit_count = models.PositiveIntegerField(default=0, help_text="Number of visits")
    visit_cost = models.DecimalField(max_digits=10, decimal_places=2, default=0.0, help_text="Cost per visit")
    bounce_count = models.PositiveIntegerField(default=0, help_text="Number of bounces")

    def __str__(self):
        return f"Visits for {self.landing_page.title}"

class VisitDetail(models.Model):
    visit = models.ForeignKey(Visit, on_delete=models.CASCADE, related_name="details", help_text="Related visit")
    device_type = models.CharField(max_length=50, choices=[("PC", "PC"), ("Mobile", "Mobile")], help_text="Device type of the visitor")
    ip_address = models.GenericIPAddressField(help_text="IP address of the visitor")
    session_start = models.DateTimeField(help_text="Session start time")
    session_end = models.DateTimeField(help_text="Session end time")
    exit_y_coordinate = models.PositiveIntegerField(null=True, blank=True, help_text="Y coordinate of the page where the visitor exited")

    def __str__(self):
        return f"Details for visit {self.visit.id}"

class Application(models.Model):
    landing_page = models.ForeignKey(LandingPage, on_delete=models.CASCADE, related_name="applications", help_text="Related landing page")
    application_count = models.PositiveIntegerField(default=0, help_text="Number of applications")
    application_cost = models.DecimalField(max_digits=10, decimal_places=2, default=0.0, help_text="Cost per application")

    def __str__(self):
        return f"Applications for {self.landing_page.title}"

class ApplicationDetail(models.Model):
    application = models.ForeignKey(Application, on_delete=models.CASCADE, related_name="details", help_text="Related application")
    name = models.CharField(max_length=255, help_text="Name of the applicant")
    contact = models.CharField(max_length=50, help_text="Contact information of the applicant")
    consultation_request_time = models.DateTimeField(help_text="Requested consultation time")
    application_date = models.DateTimeField(auto_now_add=True, help_text="Date of application")
    consultation_result = models.CharField(
        max_length=50,
        choices=[
            ("Pending", "Pending"),
            ("Declined", "Declined"),
            ("Interested", "Interested"),
        ],
        default="Pending",
        help_text="Result of the consultation",
    )
    memo = models.TextField(blank=True, null=True, help_text="Additional notes or memo")

    def __str__(self):
        return f"Detail for application {self.application.id}"
