from django.db import models


class Channel(models.Model):
    name = models.CharField(primary_key=True, max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)


class Package(models.Model):
    name = models.CharField(primary_key=True, max_length=255)
    channels = models.ManyToManyField(Channel)
    created_at = models.DateTimeField(auto_now_add=True)


class Location(models.Model):
    zip_code = models.CharField(primary_key=True, max_length=5)
    packages = models.ManyToManyField(Package)
    created_at = models.DateTimeField(auto_now_add=True)


class Subscriber(models.Model):
    name = models.CharField(max_length=255)
    location = models.ForeignKey(
        Location, 
        related_name='subscriber_location',
        on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)


class PackageMap(models.Model):
    zip_code = models.CharField(max_length=5)
    package_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
