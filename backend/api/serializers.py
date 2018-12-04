from django.db.models import Min, Max
from rest_framework import serializers
from .models import *


class LCCitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ('id', 'name', 'name_unaccented', 'video_link', 'thumbnail')


class LCSerializerMini(serializers.ModelSerializer):
    city = LCCitySerializer(read_only=True)

    class Meta:
        model = LC
        fields = ('id', 'reference_name', 'city', 'gis_id')


class LCSerializerMicro(serializers.ModelSerializer):
    class Meta:
        model = LC
        fields = ('id', 'reference_name', 'unaccented_name', 'gis_id')


class CitySerializer(serializers.ModelSerializer):
    lc_set = serializers.SerializerMethodField()

    def get_lc_set(self, obj):
        lcs = LC.objects.filter(city__id=obj.id, hidden=False)
        return LCSerializerMicro(lcs, many=True).data

    class Meta:
        model = City
        fields = ('id', 'name', 'name_unaccented', 'mapX', 'mapY', 'short_desc', 'video_link', 'details', 'lc_set')


class CitySerializerMini(serializers.ModelSerializer):
    lc_set = serializers.SerializerMethodField()

    def get_lc_set(self, obj):
        lcs = LC.objects.filter(city__id=obj.id, hidden=False)
        return LCSerializerMicro(lcs, many=True).data

    class Meta:
        model = City
        fields = ('id', 'name', 'mapX', 'mapY', 'short_desc', 'lc_set')


class RegionSerializer(serializers.ModelSerializer):
    city_set = serializers.SerializerMethodField()

    def get_city_set(self, obj):
        cities = City.objects.filter(region__id=obj.id, hidden=False)
        return CitySerializerMini(cities, many=True).data

    class Meta:
        model = Region
        fields = ('id', 'name', 'order', 'city_set')


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name', 'description', 'shortname', 'details', 'gis_id', 'logo', 'color')


class SubproductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subproduct
        fields = ('id', 'name', 'description', 'gis_id', 'product', 'logo', 'thumbnail', 'video_link')


class SDGSerializer(serializers.ModelSerializer):
    class Meta:
        model = SDG
        fields = ('id', 'name', 'description', 'gis_id', 'logo')


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('id', 'name', 'description', 'sdg', 'logo', 'thumbnail', 'video_link', 'hidden')


# class SDGandProjectsSerializer(serializers.ModelSerializer):
#     project_set = ProjectSerializer(many=True)
#
#     class Meta:
#         model = SDG
#         fields = ('id', 'name', 'description', 'gis_id', 'logo', 'project_set')


class LCSerializer(serializers.ModelSerializer):
    city = LCCitySerializer(read_only=True)
    products = ProductSerializer(many=True)
    # projects = ProjectSerializer(many=True)
    # subproducts = SubproductSerializer(many=True)

    class Meta:
        model = LC
        fields = ('id', 'reference_name', 'unaccented_name', 'gis_id', 'city', 'products')


class EntityPartnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = EntityPartner
        fields = ('id', 'entity_name', 'partnership_name', 'video_link', 'gis_id')


class OpportunitySerializer(serializers.ModelSerializer):
    lc = LCSerializerMini(read_only=True)
    response_time = serializers.SerializerMethodField()
    standards_delivery = serializers.SerializerMethodField()

    def get_response_time(self, obj):
        try:
            delta = ResponseTime.objects.get(lc=obj.lc, product=obj.product).response_time
            days, hours = delta.days, delta.seconds // 3600

            if days > 0:
                return f'{days} days'
            else:
                return f'{hours} hours'

        except ResponseTime.DoesNotExist:
            return None

    def get_standards_delivery(self, obj):
        try:
            rating_range = StandardsDelivery.objects.filter(product=obj.product)
            min = rating_range.aggregate(Min('standards_delivery_percent'))['standards_delivery_percent__min']
            max = rating_range.aggregate(Max('standards_delivery_percent'))['standards_delivery_percent__max']
            rating = rating_range.get(lc=obj.lc)

            try:
                adjusted_rating = round(round(((rating.standards_delivery_percent - min) / (max - min)) * 10) / 2)
            except ZeroDivisionError:
                adjusted_rating = 5

            return {"rating": adjusted_rating, "responses": rating.responses}

        except StandardsDelivery.DoesNotExist:
            return None

    class Meta:
        model = Opportunity
        fields = ('id', 'gis_id', 'title', 'organization_name', 'organization_gis_id', 'picture_url', 'location',
                  'duration', 'start_date', 'end_date', 'close_date', 'available_openings', 'created_at', 'updated_at',
                  'lc', 'response_time', 'standards_delivery')
