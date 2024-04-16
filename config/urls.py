from django.contrib import admin
from django.urls import path, include
from apps.post.views import PostViewSet
from apps.image.views import ImageViewSet
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static

router = routers.DefaultRouter()
router.register(r'posts',PostViewSet)
router.register(r'images',ImageViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
 