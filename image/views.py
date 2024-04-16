from rest_framework import viewsets
from image.models import Image
from image.serializer import ImageSerializer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

class ImageViewSet(viewsets.ModelViewSet):
    """Imagens"""
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    