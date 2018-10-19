from django.core.management import BaseCommand

from api.gisconnector.apicall import gis_get_rest
from api.models import Entity


class Command(BaseCommand):
    help = "Acquires MCs from the GIS and saves them to the database"

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        self.stdout.write("Initializing script.")

        # TODO: Handle exceptions
        mcs = gis_get_rest("lists/mcs_alignments.json?mc_id=495", silent=False,
                           print_function=self.stdout.write)

        for mc in mcs:
            mc_db, created = Entity.objects.get_or_create(gis_id=mc['id'], defaults={'entity_name': mc['name']})

            if created:
                self.stdout.write("Created entity " + str(mc_db.gis_id))
            else:
                self.stdout.write(str(mc_db.gis_id) + " already exists on DB")

