from csv import DictReader
from django.core.management import BaseCommand

from tds_rampup.models import Channel, Package

class Command(BaseCommand):

    def handle(self, *args, **options):

        for row in DictReader(open('./packages.csv')):
            if Channel.objects.filter(pk=row['channel_name']).exists():
                next
            else:    
                channel = Channel(name=row['channel_name'])
                channel.save()
        
        for row in DictReader(open('./packages.csv')):
            if Package.objects.filter(pk=row['pkg_name']).exists():
                next
            else:
                pkg = Package.objects.create(name=row['pkg_name'])
                channel = Channel.objects.filter(name=row['channel_name'])
                pkg.channels.set(channel)
