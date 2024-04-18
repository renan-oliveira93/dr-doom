from rest_framework import viewsets
from apps.customization.models import Customization
from apps.customization.serializer import CustomizationSerializer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

class CustomizationViewSet(viewsets.ModelViewSet):
    """Customização"""
    queryset = Customization.objects.all()
    serializer_class = CustomizationSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    