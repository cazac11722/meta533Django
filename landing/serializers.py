from rest_framework import serializers
from .models import LandingPage, Visit, VisitDetail, Application, ApplicationDetail

       
class VisitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visit
        fields = ['id', 'visit_count', 'visit_cost', 'bounce_count']


class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = ['id', 'application_count', 'application_cost']

class LandingPageSerializer(serializers.ModelSerializer):
    visits_data = VisitSerializer(many=True, read_only=True, source='visits')
    applications_data = ApplicationSerializer(many=True, read_only=True, source='applications')

    class Meta:
        model = LandingPage
        fields = [
            'id',
            'user',
            'title',
            'url',
            'ad_platform',
            'start_date',
            'end_date',
            'ad_cost',
            'html_content',
            'visits_data',
            'applications_data',
        ]
 
class VisitDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = VisitDetail
        fields = "__all__"

class ApplicationDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplicationDetail
        fields = "__all__"



class ApplicationDetailUserFindSerializer(serializers.ModelSerializer):
    applications_data = ApplicationDetailSerializer(many=True, read_only=True, source='details')

    class Meta:
        model = Application
        fields = [
            'id',
            'application_count',
            'application_cost',
            'applications_data',
        ]

class ApplicationDetailUserSerializer(serializers.ModelSerializer):
    applications_data = ApplicationDetailUserFindSerializer(many=True, read_only=True, source='applications')

    class Meta:
        model = LandingPage
        fields = [
            'id',
            'user',
            'applications_data',
        ]