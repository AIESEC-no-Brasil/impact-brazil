from django.contrib.postgres.fields import IntegerRangeField
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


# In the future, we might want to add more indexes to this file.

# Country partners
class EntityPartner(models.Model):
    entity_name = models.CharField('Entity Name', max_length=50)
    gis_id = models.IntegerField('MC ID on GIS', unique=True)
    partnership_name = models.CharField('Partnership Name', max_length=50, default='')
    video_link = models.TextField('Partnership Video ID (YouTube)', blank=True)
    thumbnail = models.CharField('Thumbnail Filename (.jpg, HD)', blank=True, max_length=256)

    def __str__(self):
        return self.entity_name

    class Meta:
        verbose_name = 'Entity partner'


# List of entities
class Entity(models.Model):
    entity_name = models.CharField('Entity Name', max_length=50)
    gis_id = models.IntegerField('MC ID on GIS', unique=True)

    def __str__(self):
        return self.entity_name

    class Meta:
        verbose_name_plural = "Entities"


class Product(models.Model):
    name = models.CharField('Product Name', max_length=50)
    shortname = models.CharField('Product Short Name', max_length=50)
    description = models.TextField('Product Description')
    details = models.TextField('Long Description')
    gis_id = models.IntegerField('Product ID on GIS', unique=True)
    logo = models.TextField('Product Logo Filename', blank=True)

    def __str__(self):
        return self.name


class VisaDenial(models.Model):
    entity = models.ForeignKey(Entity, to_field='gis_id', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, to_field='gis_id', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.entity.entity_name} - {self.product.name}'

    class Meta:
        unique_together = ('entity', 'product')


class SDG(models.Model):
    number = models.IntegerField('SDG Number', unique=True)
    name = models.CharField('SDG Name', max_length=50)
    gis_id = models.IntegerField('SDG ID on GIS', unique=True)
    description = models.TextField('SDG Description', blank=True)
    logo = models.TextField('SDG Logo', blank=True)
    hidden = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.number}: {self.name}'

    class Meta:
        verbose_name = 'SDG'


class Subproduct(models.Model):
    name = models.CharField('Subproduct Name', max_length=50)
    gis_id = models.IntegerField('Subproduct ID on GIS', unique=True)
    product = models.ForeignKey(Product, to_field='gis_id', on_delete=models.SET_NULL, null=True)
    logo = models.TextField('Subproduct Logo', blank=True)
    description = models.TextField('Subproduct Description', blank=True)
    video_link = models.CharField('Video ID (YouTube)', max_length=256, blank=True)
    thumbnail = models.CharField('Thumbnail Filename (.jpg)', blank=True, max_length=256)
    hidden = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.name} ({self.product.shortname})'


class Project(models.Model):
    name = models.CharField('Project Name', max_length=50)
    sdg = models.ForeignKey(SDG, to_field='number', on_delete=models.SET_NULL, null=True)
    description = models.TextField('Project Description', blank=True)
    logo = models.TextField('Project Logo', blank=True)
    video_link = models.CharField('Video ID (YouTube)', max_length=256, blank=True)
    thumbnail = models.CharField('Thumbnail Filename (.jpg)', blank=True, max_length=256)
    hidden = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Region(models.Model):
    name = models.CharField(max_length=255)
    order = models.IntegerField()

    def __str__(self):
        return self.name


class City(models.Model):
    name = models.CharField(max_length=255)
    name_unaccented = models.CharField("Name without special characters", max_length=255)
    mapX = models.IntegerField("Map X")
    mapY = models.IntegerField("Map Y")
    region = models.ForeignKey(Region, on_delete=models.SET_NULL, null=True)
    short_desc = models.TextField("Tagline (Short)")
    details = models.TextField("Details (Long)")
    video_link = models.CharField('Video ID (YouTube)', max_length=256, blank=True)
    thumbnail = models.CharField('Thumbnail Filename (.jpg)', blank=True, max_length=256)
    hidden = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Cities"


class LC(models.Model):
    name = ''  # Get this from GIS
    reference_name = models.CharField('LC Name', max_length=50)
    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True)
    # city_name = models.CharField('City Name', max_length=50)
    gis_id = models.IntegerField('LC ID on GIS', unique=True)
    products = models.ManyToManyField(Product, blank=True)
    subproducts = models.ManyToManyField(Subproduct, blank=True)
    # sdgs = models.ManyToManyField(SDG, verbose_name='SDG', blank=True)
    projects = models.ManyToManyField(Project, blank=True)
    searchtool_link = models.CharField(max_length=255,blank=True)
    hidden = models.BooleanField(default=False)

    # video_link = models.CharField('Video ID (YouTube)', max_length=256, blank=True)
    # thumbnail = models.CharField('Thumbnail Filename (.jpg)', blank=True, max_length=256)

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

    # Numbers & dates
    duration = models.IntegerField('Duration')
    start_date = models.DateField('Start Date')
    end_date = models.DateField('End Date')
    close_date = models.DateField('Close Date')
    available_openings = models.IntegerField('Available Openings')
    created_at = models.DateTimeField('Created At')
    updated_at = models.DateTimeField('Updated At')

    def __str__(self):
        return f'{self.title} - {self.organization_name}'

    class Meta:
        verbose_name_plural = "Opportunities"
        indexes = [
            models.Index(fields=['lc']),
            models.Index(fields=['product']),
            models.Index(fields=['subproduct']),
            models.Index(fields=['sdg'])
        ]


class Focus(models.Model):
    lc = models.ForeignKey(LC, to_field='gis_id', on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    rank = models.IntegerField(validators=[MaxValueValidator(6), MinValueValidator(1)])

    def __str__(self):
        return f'{self.lc.reference_name} - {self.product.shortname} - {self.rank}'

    class Meta:
        verbose_name_plural = "Focuses"
        unique_together = ('lc', 'product')


class Analytic(models.Model):
    lc = models.ForeignKey(LC, on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    type = models.CharField('ICX or OGX', default='icx', max_length=3)
    stage = models.CharField('CF Stage', default='APD', max_length=3)
    number = models.IntegerField('Analytic')

    def __str__(self):
        return f'{self.lc.reference_name} - {self.product.shortname} {self.type} - {self.stage}: {self.number}'

    class Meta:
        unique_together = ('lc', 'product')
        pass


class ResponseTime(models.Model):
    lc = models.ForeignKey(LC, to_field='gis_id', on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    response_time = models.DurationField()
    hidden = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.lc.reference_name} {self.product.shortname}: {self.response_time}'

    class Meta:
        unique_together = ('lc', 'product')


class StandardsDelivery(models.Model):
    lc = models.ForeignKey(LC, to_field='gis_id', on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    standards_delivery_percent = models.IntegerField()
    responses = models.IntegerField()
    hidden = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.lc.reference_name} {self.product.shortname}: {self.standards_delivery_percent}%'

    class Meta:
        unique_together = ('lc', 'product')
        verbose_name = "Standard delivery percentage"
        verbose_name_plural = "Standard delivery percentages"


class OpportunityCache(models.Model):
    opp_id = models.IntegerField("Opportunity ID", unique=True)
    opp_json = models.TextField("Opportunity JSON")

    def __str__(self):
        return f'Cache {self.opp_id}'
