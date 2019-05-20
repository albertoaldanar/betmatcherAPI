"""User models admin"""

#Django
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

#Models
from cride.users.models import User


class CustomUserAdmin(UserAdmin):
  """User admin"""

  list_display = ("email", "username", "first_name", "country")
  list_filter = ("created", "modified", "username")

admin.site.register(User, CustomUserAdmin)
