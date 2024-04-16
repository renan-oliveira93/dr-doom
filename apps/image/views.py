from rest_framework import viewsets
from apps.image.models import Image
from apps.image.serializer import ImageSerializer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

class ImageViewSet(viewsets.ModelViewSet):
    """Imagens"""
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    