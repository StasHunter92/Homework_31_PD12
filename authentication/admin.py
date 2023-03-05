from django.contrib import admin

from authentication.models import User

# ----------------------------------------------------------------------------------------------------------------------
# Register models
admin.site.register(User)
