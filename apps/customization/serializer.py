from rest_framework import serializers
from apps.customization.models import Styles, Logo, Customization

class StylesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Styles
        fields = ['id', 'primary_color', 'secondary_color', 'tertiary_color']

class LogoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Logo
        fields = ['id', 'logo']

class CustomizationSerializer(serializers.ModelSerializer):
    styles = StylesSerializer()
    logo = LogoSerializer()

    class Meta:
        model = Customization
        fields = ['styles', 'logo']

    def get_styles_data(self, instance):
        styles_instance, _ = Styles.objects.get_or_create(**instance.get('styles'))
        styles_serializer = StylesSerializer(styles_instance)
        return styles_serializer.data

    def get_logo_data(self, instance):
        logo_instance, _ = Logo.objects.get_or_create(**instance.get('logo'))
        logo_serializer = LogoSerializer(logo_instance)
        return logo_serializer.data

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['styles'] = self.get_styles_data(instance)
        representation['logo'] = self.get_logo_data(instance)
        return representation