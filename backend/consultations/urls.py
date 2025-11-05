from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

app_name = 'consultations'
router = DefaultRouter()
router.register(r'', views.ConsultationViewSet, basename='consultation')
urlpatterns = [path('', include(router.urls))]
