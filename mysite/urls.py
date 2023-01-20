from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from website.views import (
    OpenAIPhotoCreateAPIView,
    OpenAIPhotoListAPIView
)

urlpatterns = [
    path('api/openai-photo/create',OpenAIPhotoCreateAPIView.as_view(),name='api-openai-create'),
    path('api/openai-photo/list',OpenAIPhotoListAPIView.as_view(),name='api-openai-list'),
] +static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)