from django.contrib import admin
from. models import Driver, DriverCart, Rating
class DriverAdmin(admin.ModelAdmin):
    list_display = ('user', 'id', 'deriction', 'automobile', 'phone_number_one', 'phone_number_two', 'cooling_system', 'baggage', 'fuel', 'sex', 'create_at', 'status',)

class DriverCartAdmin(admin.ModelAdmin):
    list_display = ('driver', 'id', 'current_location', 'finish_location', 'empty_count', 'delivery', 'create_at', 'status',)

admin.site.register(Driver, DriverAdmin )
admin.site.register(DriverCart, DriverCartAdmin)
admin.site.register(Rating)
