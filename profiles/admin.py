"""
This module registers the profiles app model to the admin.
"""
from django.contrib import admin

from profiles.models import Profile


admin.site.register(Profile)
