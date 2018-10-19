from pkgutil import get_data

from django.core.management import BaseCommand

from api.gisconnector.apicall import gis_get_data
from api.models import Product, SDG, Subproduct, LC


class Command(BaseCommand):
    help = "Acquires analytics from the GIS and saves them to the database"

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        get_all_lcs_gql = "get_all_lcs.gql"

        self.stdout.write("Initializing script.")

        # TODO: Handle exceptions
        lcs = gis_get_data(get_data("api.gql", get_all_lcs_gql).decode("utf-8"),
                           silent=False, print_function=self.stdout.write)

        # We use .filter().first() instead of .get() because if there's no corresponding subproduct/SDG, then it returns
        # None instead of an exception
        for lc in lcs:
            lc_db, created = LC.objects.get_or_create(gis_id=lc['id'], defaults={'reference_name': lc['name']})

            if created:
                lc_db.products.add(*Product.objects.all())
                lc_db.subproducts.add(*Subproduct.objects.all())
                lc_db.sdgs.add(*SDG.objects.all())
                self.stdout.write("Created LC " + str(lc_db.gis_id))
            else:
                self.stdout.write(str(lc_db.gis_id) + " already exists on DB")
