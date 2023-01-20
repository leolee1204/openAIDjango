from django.urls import path, include, re_path
from rest_framework.routers import DefaultRouter
from django.views.generic import TemplateView

# from views.api import BasicDataViewSet

router = DefaultRouter()
# router.register('', BasicDataViewSet, basename='api')
app_name = 'website'

urlpatterns = [
    path('', include(router.urls)),

]