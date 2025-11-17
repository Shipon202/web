from django.contrib import admin
from hotel.models import HotelStore
# Register your models here.
class HotelStoreModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'hotel_name', 'owner_name')

admin.site.register(HotelStore,HotelStoreModelAdmin)