from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.views import CategoryViewSet, JobViewSet

app_name = 'api'

router_v1 = DefaultRouter()
router_v1.register(r'jobs', JobViewSet, basename='jobs')
router_v1.register(r'category', CategoryViewSet, basename='category')

urlpatterns = [
    path('', include(router_v1.urls)),
]
