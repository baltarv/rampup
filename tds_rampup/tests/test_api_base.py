from django.test import TestCase
from tds_rampup.models import Subscriber, Location, Package, Channel


class APIMixin:

    def make_channel(self):
        return Channel.objects.create(name='channel-test')
    
    def make_package(self):
        pkg = Package.objects.create(name='package-test')
        channel = Channel.objects.filter(pk='channel-test')
        pkg.channels.set(channel)
        return pkg

    def make_location(self, zip_code='12345'):
        location = Location.objects.create(zip_code=zip_code)
        package = Package.objects.filter(pk='package-test')
        location.packages.set(package)
        return location
    
    def make_subscriber(self, name='subscriber-test'):

        location = self.make_location()
        subscriber = Subscriber.objects.create(
            name=name, 
            location=location
        )
        return subscriber

    def make_subscribers_in_batch(self, qtd=10):
        subscribers = []
        location = self.make_location()
        for i in range(qtd):
            subscriber = Subscriber.objects.create(
                name=f'subscriber-test-{i}', 
                location=location
            )
            subscribers.append(subscriber)
        return subscribers


class APITestBase(TestCase, APIMixin):
    def setUp(self) -> None:
        return super().setUp()
