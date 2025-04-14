from django.contrib import admin

# Register your models here.

from .models import Listing

class ListingAdmin(admin.ModelAdmin):
    pass

admin.site.register(Listing, ListingAdmin)