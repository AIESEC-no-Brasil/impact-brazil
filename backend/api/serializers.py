from rest_framework import serializers
from .models import LC, Product, SDG, Subproduct, EntityPartner, Opportunity


class LCSerializer(serializers.ModelSerializer):
    class Meta:
        model = LC
        fields = ('id', 'reference_name', 'city', 'gis_id', 'video_link', 'thumbnail', 'products', 'subproducts', 'sdgs')


class LCSerializerMini(serializers.ModelSerializer):
    class Meta:
        model = LC
        fields = ('id', 'reference_name', 'city', 'gis_id', 'video_link', 'thumbnail')


class ProductSerializer(serializers.ModelSerializer):
    lc_set = LCSerializerMini(many=True)

    class Meta:
        model = Product
        fields = ('id', 'name', 'description', 'shortname', 'gis_id', 'lc_set', 'logo')


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

    class Meta:
        model = Opportunity
        fields = ('id', 'gis_id', 'title', 'organization_name', 'organization_gis_id', 'picture_url', 'location', 'duration', 'start_date', 'available_openings', 'created_at', 'updated_at', 'lc')
