from rest_framework import serializers
from image.models import Image

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['id', 'title', 'credits', 'picture_date', 'picture']