from django.contrib import admin
from .models import Publication

class PublicationAdmin(admin.ModelAdmin):
    list_display        = ["title",
                           "description",
                           "publisher",
                           "publication_date",
                           "link"]
    list_filter         = ["publisher"]
    search_fields       = ["title"]

# Register your models here.
admin.site.register(Publication, PublicationAdmin)
