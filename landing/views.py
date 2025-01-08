from rest_framework import viewsets
from .models import LandingPage, Visit, VisitDetail, Application, ApplicationDetail
from .serializers import LandingPageSerializer, VisitSerializer, VisitDetailSerializer, ApplicationSerializer, ApplicationDetailSerializer, ApplicationDetailUserSerializer

class LandingPageViewSet(viewsets.ModelViewSet):
    queryset = LandingPage.objects.all()
    serializer_class = LandingPageSerializer

    def perform_create(self, serializer):
        """
        LandingPage가 생성되면 관련 Visit 및 Application 데이터를 자동으로 생성.
        """
        # LandingPage 객체를 저장
        landing_page = serializer.save()

        # Visit 객체 생성
        Visit.objects.create(
            landing_page=landing_page,
            visit_count=0,
            visit_cost=0.0,
            bounce_count=0
        )

        # Application 객체 생성
        Application.objects.create(
            landing_page=landing_page,
            application_count=0,
            application_cost=0.0
        )

class LandingPageUrlViewSet(viewsets.ModelViewSet):
    serializer_class = LandingPageSerializer

    def get_queryset(self):
        """
        URL 경로에서 'user' 값을 가져와 해당 사용자의 데이터를 필터링합니다.
        """
        url = self.kwargs.get('url')  # URL의 <int:user>에서 값 가져오기
        if url:
            return LandingPage.objects.filter(url=url)

class LandingPageUserViewSet(viewsets.ModelViewSet):
    serializer_class = LandingPageSerializer

    def get_queryset(self):
        """
        URL 경로에서 'user' 값을 가져와 해당 사용자의 데이터를 필터링합니다.
        """
        user_id = self.kwargs.get('user')  # URL의 <int:user>에서 값 가져오기
        if user_id:
            return LandingPage.objects.filter(user_id=user_id)

class VisitViewSet(viewsets.ModelViewSet):
    queryset = Visit.objects.all()
    serializer_class = VisitSerializer

class VisitDetailViewSet(viewsets.ModelViewSet):
    queryset = VisitDetail.objects.all()
    serializer_class = VisitDetailSerializer

    def perform_create(self, serializer):
        """
        VisitDetail 생성 시 관련 Visit 데이터를 업데이트합니다.
        """
        visit_detail = serializer.save()
        visit = visit_detail.visit

        # Visit 데이터 업데이트
        visit.visit_count += 1  if visit_detail.exit_y_coordinate <= 0 else 0
        visit.visit_cost += 10  # 예: visit_detail에 비용이 포함되어 있다고 가정
        visit.bounce_count += 1 if visit_detail.exit_y_coordinate else 0  # 이탈 여부 계산
        visit.save()


class ApplicationViewSet(viewsets.ModelViewSet):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer

class ApplicationDetailViewSet(viewsets.ModelViewSet):
    queryset = ApplicationDetail.objects.all()
    serializer_class = ApplicationDetailSerializer

    def perform_create(self, serializer):
        """
        ApplicationDetail 생성 시 관련 Application 데이터를 업데이트합니다.
        """
        application_detail = serializer.save()
        application = application_detail.application

        # Application 데이터 업데이트
        application.application_count += 1
        application.application_cost += 100  # 예: 신청당 비용이 고정된 값이라고 가정
        application.save()

class ApplicationUserViewSet(viewsets.ModelViewSet):
    serializer_class = ApplicationDetailUserSerializer

    def get_queryset(self):
        """
        URL 경로에서 'user' 값을 가져와 해당 사용자의 데이터를 필터링합니다.
        """
        user_id = self.kwargs.get('user')  # URL의 <int:user>에서 값 가져오기
        if user_id:
            data_list = LandingPage.objects.filter(user=user_id)

            return data_list
