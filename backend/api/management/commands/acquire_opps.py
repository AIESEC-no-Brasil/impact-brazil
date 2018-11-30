from pkgutil import get_data

import iso8601 as iso8601
from django.core.management import BaseCommand

from api.gisconnector.apicall import gis_get_paginated
from api.models import Opportunity, Product, SDG, Subproduct, LC


# Convert GIS date format to Python
def date_to_db(date, date_only=True):
    parsed_date = iso8601.parse_date(date)
    if date_only:
        return parsed_date.strftime("%Y-%m-%d")
    else:
        return parsed_date.strftime("%Y-%m-%d %H:%m:%s%z")


class Command(BaseCommand):
    help = "Acquires opportunities from the GIS and saves them to the database"

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        get_all_opportunities_gql = "get_all_opportunities.gql"

        self.stdout.write("Initializing script.")

        # TODO: Handle exceptions
        opportunities = gis_get_paginated(get_data("api.gql", get_all_opportunities_gql).decode("utf-8"), silent=False,
                                          print_function=self.stdout.write)
        # opportunities = expa_get(get_data("api.gql", get_all_opportunities_gql).decode("utf-8").replace("$PAGE$", "1")
        #                          ,silent=False, print_function=self.stdout.write)

        # We use .filter().first() instead of .get() because if there's no corresponding subproduct/SDG, then it returns
        # None instead of an exception
        for opp in opportunities['data']:
            try:
                product = Product.objects.filter(gis_id=opp['programme']['id']).first()
            except TypeError:
                product = None

            try:
                sdg = SDG.objects.filter(number=opp['sdg_info']['sdg_target']['goal_index']).first()  # Weird GIS
            except TypeError:
                sdg = None

            try:
                subproduct = Subproduct.objects.filter(gis_id=opp['sub_product']['id']).first()
            except TypeError:
                subproduct = None

            opp_data = {
                'title': opp['title'],
                'lc': LC.objects.get(gis_id=opp['home_lc']['id']),
                'product': product,
                'sdg': sdg,
                'subproduct': subproduct,
                'organization_name': opp['organisation']['name'],
                'organization_gis_id': opp['organisation']['id'],
                'picture_url': opp['cover_photo'],
                'location': opp['location'],
                'duration': opp['duration'],
                'start_date': date_to_db(opp['earliest_start_date'], date_only=True),
                'end_date': date_to_db(opp['latest_end_date'], date_only=True),
                'close_date': date_to_db(opp['applications_close_date'], date_only=True),
                'available_openings': opp['available_openings'],
                'created_at': opp['created_at'],
                'updated_at': opp['updated_at']
            }
            opp_db, created = Opportunity.objects.get_or_create(gis_id=opp['id'], defaults={**opp_data})

            if created:
                self.stdout.write("Created opp " + str(opp_db.gis_id))
            else:
                # Check if the opp was updated
                if opp_db.updated_at < iso8601.parse_date(opp['updated_at']):
                    # Nope, we need to update it!
                    new_opp = {'id': opp_db.id, 'gis_id': opp_db.gis_id, **opp_data}
                    new_opp_created = Opportunity(**new_opp)
                    new_opp_created.save()
                    self.stdout.write("Updated opp " + str(new_opp_created.gis_id))
                else:
                    self.stdout.write("Ignoring " + str(opp_db.gis_id) + " since there were no changes")
