from datetime import date

from django.core.management import BaseCommand

from api.gisconnector.apicall import gis_get_paginated, gis_get, gis_get_data, gis_get_rest
from api.models import Opportunity, Product, SDG, Subproduct, LC, Analytic


class Command(BaseCommand):
    help = "Acquires analytics from the GIS and saves them to the database"

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        saved_analytic = "i_approved_"

        self.stdout.write("Initializing script.")

        lcs = LC.objects.all()

        for lc in lcs:
            year = date.today().year
            start_date = str(year) + "-02-01"  # Change this if LC cycle changes
            end_date = str(year + 1) + "-01-31"
            analytics = gis_get_rest(f"applications/analyze.json?start_date={start_date}&end_date={end_date}"
                                     f"&performance[office_id]={lc.gis_id}", silent=False,
                                     print_function=self.stdout.write)

            for product in lc.products.all():
                prod_name = saved_analytic + product.shortname.lower()
                try:
                    doc_count = analytics['analytics'][prod_name]['doc_count']
                except KeyError:
                    self.stdout.write(f"{prod_name} for {lc.reference_name} not found, skipping")
                else:
                    analytic, created = Analytic.objects.update_or_create(lc=lc, product=product,
                                                                          defaults={'number': doc_count})

                    if created:
                        self.stdout.write(f"{prod_name} for {lc.reference_name} created as {analytic.number}")
                    else:
                        self.stdout.write(f"{prod_name} for {lc.reference_name} updated to {analytic.number}")
