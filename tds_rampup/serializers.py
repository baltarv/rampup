from rest_framework import serializers

from .models import Subscriber, Location


class SubscriberSerializer(serializers.ModelSerializer):

    class Meta:
        model = Subscriber
        fields = ('id', 'name', 'location')


class LocationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Location
        fields = ('zip_code', 'packages')
