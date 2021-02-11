from django.core.exceptions import ObjectDoesNotExist

from rest_framework import status

from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from api.ipstack_config import geo_lookup
from data.models import GeoLocationData
from data.serializers import GeoLocationDataSerializer


class GeoLocationDataViewSet(ModelViewSet):
    queryset = GeoLocationData.objects.all()
    serializer_class = GeoLocationDataSerializer
    permission_classes = (IsAuthenticated,)

    def create(self, request, *args, **kwargs):
        ip_address = request.META.get("REMOTE_ADDR")
        try:
            location = geo_lookup.get_location(ip_address)
            if location is None:
                return Response({"Error": "Failed to find location."}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            print(e)
            return Response({"Error": "IPStack API is unavailable, please try again later."}, status=500)
        serializer = self.serializer_class(data=dict(location))
        if serializer.is_valid():
            serializer.save()
            return Response(dict(location), status=status.HTTP_201_CREATED)
        else:
            print(serializer.errors)
            return Response({"Error": "Unable to add entry to database"}, status=status.HTTP_400_BAD_REQUEST)

    def list(self, request, *args, **kwargs):
        ip_address = request.META.get("REMOTE_ADDR")
        try:
            obj = GeoLocationData.objects.get(ip=ip_address)
            serializer = self.serializer_class(obj)
            return Response(serializer.data, status=200)
        except ObjectDoesNotExist:
            return Response({"Error": "No entries in database for your ip."}, status=status.HTTP_404_NOT_FOUND)

    def destroy(self, request, *args, **kwargs):
        ip_address = request.META.get("REMOTE_ADDR")
        if ip_geolocation_entry := self.queryset.filter(ip=ip_address):
            ip_geolocation_entry.delete()
            return Response({"Success": f"Geolocation data entry for {ip_address} successfully deleted."}, status=status.HTTP_200_OK)
        return Response({"Error": f"No entry in database for {ip_address}."}, status=status.HTTP_404_NOT_FOUND)
