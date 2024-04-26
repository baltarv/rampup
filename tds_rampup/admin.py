from django.contrib import admin

from .models import Channel, Location, Subscriber, Package, PackageMap


@admin.register(Channel)
class ChannelAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ['zip_code']


@admin.register(Subscriber)
class SubscriberAdmin(admin.ModelAdmin):
    list_display = ['name', 'location']


@admin.register(Package)
class PackageAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(PackageMap)
class PackageMapAdmin(admin.ModelAdmin):
    list_display = ['zip_code', 'package_name']
