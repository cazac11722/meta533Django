from django.urls import path
from .views import LandingPageViewSet, LandingPageUserViewSet,LandingPageUrlViewSet, VisitViewSet, VisitDetailViewSet, ApplicationViewSet, ApplicationDetailViewSet

urlpatterns = [
    path('landing-pages/', LandingPageViewSet.as_view({'get': 'list', 'post': 'create'}), name='landing-page-list-create'),
    path('landing-pages/<int:pk>/', LandingPageViewSet.as_view({'get': 'retrieve'}), name='landing-page-detail'),
    path('landing-pages/url/<str:url>/', LandingPageUrlViewSet.as_view({'get': 'list'}), name='landing-page-url-list'),
    path('landing-pages/user/<int:user>/', LandingPageUserViewSet.as_view({'get': 'list'}), name='landing-page-user-list'),

    path('visits/', VisitViewSet.as_view({'get': 'list', 'post': 'create'}), name='visit-list-create'),
    path('visits/<int:pk>/', VisitViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='visit-detail'),

    path('visit-details/', VisitDetailViewSet.as_view({'get': 'list', 'post': 'create'}), name='visit-detail-list-create'),
    path('visit-details/<int:pk>/', VisitDetailViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='visit-detail-detail'),

    path('applications/', ApplicationViewSet.as_view({'get': 'list', 'post': 'create'}), name='application-list-create'),
    path('applications/<int:pk>/', ApplicationViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='application-detail'),

    path('application-details/', ApplicationDetailViewSet.as_view({'get': 'list', 'post': 'create'}), name='application-detail-list-create'),
    path('application-details/<int:pk>/', ApplicationDetailViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='application-detail-detail'),
]