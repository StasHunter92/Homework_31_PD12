from django.contrib import admin

from ads.models import Advertisement, Category

# ----------------------------------------------------------------------------------------------------------------------
# Register models
admin.site.register(Advertisement)
admin.site.register(Category)
