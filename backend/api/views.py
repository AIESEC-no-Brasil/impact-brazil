import json
from builtins import str

import requests
from django.core import serializers
from django.db.models import Max
from django.shortcuts import render, get_object_or_404
from rest_framework import status, generics, exceptions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.serializers import ValidationError

from api.models import EntityPartner, LC, Product, Subproduct, SDG, Opportunity, Focus, Analytic, Entity
from api.serializers import LCSerializer, SubproductSerializer, ProductSerializer, SDGSerializer, \
    EntityPartnerSerializer, OpportunitySerializer


# Get the list of entities, prioritizing country partners
class EntityList(APIView):
    def get(self, request, format=None):
        # Get entity list
        gis_list = Entity.objects.all()

        # Get country partners
        entity_partners_list = []
        for entity in EntityPartner.objects.all():
            entity_partners_list.append(entity.entity_name)

        # We will build 2 dicts, one of entity partners and one of all other entities, then merge them
        gis_list_partners = []
        gis_list_others = []

        for entity in gis_list:
            if entity.entity_name in entity_partners_list:
                gis_list_partners.append({"id": entity.gis_id, "name": entity.entity_name})
            else:
                gis_list_others.append({"id": entity.gis_id, "name": entity.entity_name})

        # Merge the two lists, keeping entity partners on top
        gis_list = gis_list_partners + gis_list_others

        return Response(gis_list)


# Get the list of opportunities by parameter
class OpportunityList(APIView):
    # FIXME: if no opportunities are present, it breaks
    # FIXME: also, we need to figure out why most opps have no sDG
    def get(self, request, format=None):
        entity = self.request.query_params.get('entity', None)
        start_date = self.request.query_params.get('start_date', None)
        end_date = self.request.query_params.get('end_date', None)
        product = self.request.query_params.get('product', None)

        if None in (entity, start_date, end_date, product):
            raise exceptions.ParseError('entity, start_date, end_date and product must be set')

        sdg = self.request.query_params.get('sdg', None)
        subproduct = self.request.query_params.get('subproduct', None)

        if sdg is None and subproduct is None:
            raise exceptions.ParseError('Either sdg or subproduct must be set')

        sdg_or_subproduct = 'sdg' if subproduct is None else 'subproduct'

        # Build a list of one opportunity per LC, that opportunity will be the one satisfying all conditions and having
        # the highest number of available_openings

        # First, get all LCs & matching opportunities
        if sdg_or_subproduct == 'subproduct':
            lcs = LC.objects.filter(products__gis_id=product, subproducts__gis_id=subproduct)
            opportunities_list = Opportunity.objects.filter(product__gis_id=product, subproduct__gis_id=subproduct)
        else:
            lcs = LC.objects.filter(products__gis_id=product, sdgs__gis_id=sdg)
            opportunities_list = Opportunity.objects.filter(product__gis_id=product, sdg__gis_id=sdg)

        # Now, for every LC, get one opportunity
        opportunities_list = opportunities_list.distinct('lc_id').order_by('lc_id', '-available_openings')

        # Reorder according to focus in reverse so we iterate through it backwards
        focus_qs = Focus.objects.filter(product__gis_id=product).order_by('-rank').values('lc__id')
        focuses = []

        # Also reorder according to analytics, but remember that if lc1 in focus f1 > lc2 in focus f2 but lc in focus k2
        # has n2 approvals < n1 approvals of lc1, then we still show lc1 > lc2 because focus > approvals
        analytics_qs = Analytic.objects.filter(product__gis_id=product).order_by('number').values('lc__id')
        analytics = []

        # We need to build the lists
        for focus in focus_qs:
            focuses.append(focus['lc__id'])

        for analytic in analytics_qs:
            analytics.append(analytic['lc__id'])

        # Build final list
        opportunities_list_ordered = list(opportunities_list)

        for rankparam in [analytics, focuses]:
            for rank in rankparam:
                for opportunity in opportunities_list:
                    if opportunity.lc_id == rank:
                        opportunities_list_ordered.remove(opportunity)
                        opportunities_list_ordered = [opportunity] + opportunities_list_ordered

        return Response(OpportunitySerializer(opportunities_list_ordered, many=True).data)


# Get list of LCs
class LCList(generics.ListAPIView):
    queryset = LC.objects.all()
    serializer_class = LCSerializer


# Get details of LC
class LCDetails(generics.RetrieveAPIView):
    queryset = LC.objects.all()
    serializer_class = LCSerializer


# Get list of products
class ProductList(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


# Get list of subproducts
class SubproductList(generics.ListAPIView):
    def get_queryset(self):
        product = self.request.query_params.get('product', None)

        if product is None:
            return Subproduct.objects.all()
        else:
            return Subproduct.objects.filter(product__gis_id=product)

    serializer_class = SubproductSerializer


# Get list of SDGs
class SDGList(generics.ListAPIView):
    queryset = SDG.objects.all()
    serializer_class = SDGSerializer


# Get list of entity partners
class EntityPartnerList(generics.ListAPIView):
    queryset = EntityPartner.objects.all()
    serializer_class = EntityPartnerSerializer


# Get list of entity partners
class EntityPartnerDetails(APIView):
    def get(self, request, format=None, pk=0):
        try:
            entity = EntityPartner.objects.get(gis_id=pk)
            is_partner = True
        except EntityPartner.DoesNotExist:
            entity = get_object_or_404(Entity.objects.all(), gis_id=pk)
            is_partner = False

        partnership_details = {"id": entity.id, "gis_id": entity.gis_id, "name": entity.entity_name, "is_partner": is_partner, "video": None}

        if is_partner:
            partnership_details['video'] = entity.video_link

        return Response(partnership_details)


# Get the list of entities, prioritizing country partners
# class OpportunityList(APIView):
#     def get(self, request, format=None):
#         try:
#             gis_list_request = requests.get(gis_mc_list_url)
#             gis_list = json.loads(gis_list_request.text)
#         except:
#             return Response({'error': "There was a problem getting the opportunity list from the GIS."},
#                             status=status.HTTP_500_INTERNAL_SERVER_ERROR)
#         else:
#
