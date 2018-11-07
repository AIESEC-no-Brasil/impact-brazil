from django.db.models import Min, Max
from rest_framework import serializers
from .models import *


class LCSerializer(serializers.ModelSerializer):
    class Meta:
        model = LC
        fields = (
            'id', 'reference_name', 'city_name', 'gis_id', 'video_link', 'thumbnail', 'products', 'subproducts', 'sdgs')


class LCSerializerMini(serializers.ModelSerializer):
    class Meta:
        model = LC
        fields = ('id', 'reference_name', 'city_name', 'gis_id', 'video_link', 'thumbnail')


class LCSerializerMicro(serializers.ModelSerializer):
    class Meta:
        model = LC
        fields = ('id', 'reference_name', 'gis_id')


class CitySerializer(serializers.ModelSerializer):
    lc_set = LCSerializerMicro(many=True)

    class Meta:
        model = City
        fields = ('id', 'name', 'mapX', 'mapY', 'short_desc', 'video_link', 'details', 'lc_set')


class CitySerializerMini(serializers.ModelSerializer):
    lc_set = LCSerializerMicro(many=True)

    class Meta:
        model = City
        fields = ('id', 'name', 'mapX', 'mapY', 'short_desc', 'lc_set')


class ProductSerializer(serializers.ModelSerializer):
    lc_set = LCSerializerMini(many=True)

    class Meta:
        model = Product
        fields = ('id', 'name', 'description', 'shortname', 'details', 'gis_id', 'lc_set', 'logo')


class SubproductSerializer(serializers.ModelSerializer):
    lc_set = LCSerializerMini(read_only=True, many=True)

    class Meta:
        model = Subproduct
        fields = ('id', 'name', 'gis_id', 'lc_set', 'logo')


class SDGSerializer(serializers.ModelSerializer):
    lc_set = LCSerializerMini(read_only=True, many=True)

    class Meta:
        model = SDG
        fields = ('id', 'name', 'gis_id', 'lc_set', 'logo')


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
                  'duration', 'start_date', 'available_openings', 'created_at', 'updated_at', 'lc',
                  'response_time', 'standards_delivery')
