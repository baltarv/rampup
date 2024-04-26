from csv import DictReader
from django.core.management import BaseCommand

from tds_rampup.models import PackageMap

class Command(BaseCommand):

    def handle(self, *args, **options):

        for row in DictReader(open('./zip_to_package_map.csv')):
            if PackageMap.objects.filter(pk=row['zip_code']).exists():
                next
            else:
                package_map = PackageMap(
                    zip_code=row['zip_code'],
                    package_name=row['pkg_name']
                )
                package_map.save()
        