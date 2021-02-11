from rest_framework.serializers import ModelSerializer

from data.models import GeoLocationData


class GeoLocationDataSerializer(ModelSerializer):
    class Meta:
        model = GeoLocationData
        fields = "__all__"
