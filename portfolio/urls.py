from django.urls import path, include
from .views import PostViewSet, application_post_view
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('posts', PostViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('application-to-<str:company_name>/', application_post_view, name='application_post'),
]
