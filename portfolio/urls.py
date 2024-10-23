from django.urls import path, include
from .views import PostViewSet, application_post_view
from rest_framework.routers import DefaultRouter
from django.conf import settings
from django.conf.urls.static import static

router = DefaultRouter()
router.register('posts', PostViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('application-to-<str:company_name>/', application_post_view, name='application_post'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)