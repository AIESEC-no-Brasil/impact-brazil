from django.contrib.postgres.fields import IntegerRangeField
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


# Create your models here.

# Country partners
class EntityPartner(models.Model):
    entity_name = models.CharField('Entity Name', max_length=50)
    gis_id = models.IntegerField('MC ID on GIS')
    partnership_name = models.CharField('Partnership Name', max_length=50, default='')
    video_link = models.TextField('Partnership Video Link', blank=True)

    def __str__(self):
        return self.entity_name

    class Meta:
        verbose_name = 'Entity Partner'


# List of entities
class Entity(models.Model):
    entity_name = models.CharField('Entity Name', max_length=50)
    gis_id = models.IntegerField('MC ID on GIS')
    no_visa = models.BooleanField('No Visa for Brazil')

    def __str__(self):
        return self.entity_name

    class Meta:
        verbose_name_plural = "Entities"


class Product(models.Model):
    name = models.CharField('Product Name', max_length=50)
    shortname = models.CharField('Product Short Name', max_length=50)
    description = models.TextField('Product Description')
    gis_id = models.IntegerField('Product ID on GIS', unique=True)
    logo = models.TextField('Product Logo Filename', blank=True)

    def __str__(self):
        return self.name


class SDG(models.Model):
    number = models.IntegerField('SDG Number')
    name = models.CharField('SDG Name', max_length=50)
    gis_id = models.IntegerField('SDG ID on GIS', unique=True)
    logo = models.TextField('SDG Logo', blank=True)

    def __str__(self):
        return f'{self.number}: {self.name}'

    class Meta:
        verbose_name = 'SDG'


class Subproduct(models.Model):
    name = models.CharField('Subproduct Name', max_length=50)
    gis_id = models.IntegerField('Subproduct ID on GIS', unique=True)
    product = models.ForeignKey(Product, to_field='gis_id', on_delete=models.SET_NULL, null=True)
    logo = models.TextField('Subproduct Logo', blank=True)

    def __str__(self):
        return f'{self.name} ({self.product.shortname})'


class LC(models.Model):
    name = ''  # Get this from GIS
    reference_name = models.CharField('Name for Reference Purposes', max_length=50)
    gis_id = models.IntegerField('LC ID on GIS', unique=True)
    products = models.ManyToManyField(Product, blank=True)
    subproducts = models.ManyToManyField(Subproduct, blank=True)
    sdgs = models.ManyToManyField(SDG, verbose_name='SDG', blank=True)

    def __str__(self):
        return self.reference_name

    class Meta:
        verbose_name = 'LC'


class Opportunity(models.Model):
    # Basic details
    gis_id = models.IntegerField('Opportunity ID on GIS')
    title = models.CharField('Title', max_length=256)

    # Associations
    lc = models.ForeignKey(LC, on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    sdg = models.ForeignKey(SDG, on_delete=models.SET_NULL, null=True)
    subproduct = models.ForeignKey(Subproduct, on_delete=models.SET_NULL, null=True)

    # More details
    organization_name = models.CharField('Organization', max_length=256)
    organization_gis_id = models.IntegerField('GIS ID of Organization')
    picture_url = models.TextField('Picture URL')
    location = models.CharField('Location', max_length=256, null=True)

    # Numbers
    duration = models.IntegerField('Duration')
    start_date = models.DateField('Start Date')
    end_date = models.DateField('End Date')
    available_openings = models.IntegerField('Available Openings')
    created_at = models.DateTimeField('Created At')
    updated_at = models.DateTimeField('Updated At')

    def __str__(self):
        return f'{self.title} - {self.organization_name}'

    class Meta:
        verbose_name_plural = "Opportunities"


class Focus(models.Model):
    lc = models.ForeignKey(LC, on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    rank = models.IntegerField(validators=[MaxValueValidator(6), MinValueValidator(1)])

    def __str__(self):
        return f'{self.lc.reference_name} - {self.product.shortname} - {self.rank}'

    class Meta:
        verbose_name_plural = "Focuses"


class Analytic(models.Model):
    lc = models.ForeignKey(LC, on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    type = models.CharField('ICX or OGX', default='icx', max_length=3)
    number = models.IntegerField('Analytic')

    def __str__(self):
        return f'{self.lc.reference_name} - {self.product.shortname} {self.type}: {self.number}'
