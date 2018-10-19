from django.contrib import admin

# Register your models here.
from api.models import *

admin.site.site_header = 'Impact Brazil Admin Panel'
admin.site.site_title = 'Impact Brazil'

admin.site.register(EntityPartner)
admin.site.register(Product)
admin.site.register(Subproduct)
admin.site.register(SDG)
admin.site.register(LC)
admin.site.register(Opportunity)
admin.site.register(Focus)
admin.site.register(Analytic)