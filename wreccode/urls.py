from django import urls
from django.urls import path, include
from .views import ResponseApiView

from rest_framework.routers import DefaultRouter

# router = DefaultRouter()
# router.register('responses')


urlpatterns = [
    # path('', include(router.urls)),
    path('test/<int:pk>', ResponseApiView.as_view()),
]