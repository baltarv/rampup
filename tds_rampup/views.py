from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.shortcuts import get_object_or_404


from .models import Subscriber, Location
from .serializers import SubscriberSerializer, LocationSerializer


@api_view(http_method_names=['get', 'post'])
def subscribers_api_list(request):

    if request.method == 'GET':
        subscribers = Subscriber.objects.all()
        serializer = SubscriberSerializer(subscribers, many=True)

        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = SubscriberSerializer(
            data=request.data,
            context={'request': request}
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED
        )


@api_view(http_method_names=['get', 'post'])
def locations_api_list(request):

    if request.method == 'GET':
        locations = Location.objects.all()
        serializer = LocationSerializer(locations, many=True)
        
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = LocationSerializer(
            data=request.data,
            context={'request': request}
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED
        )


@api_view(http_method_names=['get'])
def subscriber_api_detail(request, pk):
    subscriber = get_object_or_404(
        Subscriber.objects.all(),
        pk=pk
    )

    if request.method == 'GET':
        serializer = SubscriberSerializer(
            instance=subscriber,
            many=False,
            context={'request': request}
        )

        return Response(serializer.data)


@api_view(http_method_names=['get'])
def location_api_detail(request, pk):
    location = get_object_or_404(
        Location.objects.all(),
        pk=pk
    )

    if request.method == 'GET':
        serializer = LocationSerializer(
            instance=location,
            many=False,
            context={'request': request}
        )

        return Response(serializer.data)
