from django.contrib import admin
from . models import Province, District, Automobile, Deriction, DeliveryType

admin.site.site_header = 'Boshqaruv paneli'
admin.site.site_title = 'Boshqaruv paneli'
admin.site.index_title = "Assalomu alaykum!"
admin.site.register(Province)
admin.site.register(District)
admin.site.register(Automobile)
admin.site.register(Deriction)
admin.site.register(DeliveryType)
