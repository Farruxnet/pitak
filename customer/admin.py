from django.contrib import admin
from . models import Customer

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('user', 'customer_current_province' ,'customer_current_district' ,'customer_finish_province' ,'customer_finish_district' ,'automobile' ,'passengers_count' ,'phone_number' ,'date' ,'latitude' ,'longitude' ,'sex' ,'status')
    search_fields = ['phone_number']
    raw_id_fields=('user',)


admin.site.register(Customer, CustomerAdmin)
