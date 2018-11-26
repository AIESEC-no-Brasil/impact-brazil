from django.contrib import admin

# Register your models here.
from api.models import *

admin.site.site_header = 'Impact Brazil Admin Panel'
admin.site.site_title = 'Impact Brazil'


class FocusAdmin(admin.ModelAdmin):
    list_display = ['lc', 'product', 'rank']
    list_editable = ['rank']
    ordering = ('product', 'lc')


class ResponseTimeAdmin(admin.ModelAdmin):
    list_display = ['lc', 'product', 'response_time']
    list_editable = ['response_time']
    ordering = ('product', 'lc')


class StandardsDeliveryAdmin(admin.ModelAdmin):
    list_display = ['lc', 'product', 'standards_delivery_percent', 'responses']
    list_editable = ['standards_delivery_percent', 'responses']
    ordering = ('product', 'lc')


class VisaDenialsAdmin(admin.ModelAdmin):
    ordering = ('entity', 'product')


admin.site.register(Focus, FocusAdmin)
admin.site.register(ResponseTime, ResponseTimeAdmin)
admin.site.register(StandardsDelivery, StandardsDeliveryAdmin)
admin.site.register(VisaDenial, VisaDenialsAdmin)

admin.site.register(EntityPartner)
admin.site.register(Product)
admin.site.register(Subproduct)
admin.site.register(Project)
admin.site.register(SDG)
admin.site.register(LC)
admin.site.register(Opportunity)
admin.site.register(Analytic)
admin.site.register(Entity)
admin.site.register(City)
