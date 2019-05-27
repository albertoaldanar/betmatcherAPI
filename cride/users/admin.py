"""User models admin"""

#Django
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

#Models
from cride.users.models import User, Profile


class CustomUserAdmin(UserAdmin):
  """User admin"""

  list_display = ("email", "username", "first_name", "country")
  list_filter = ("created", "modified", "username")


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("country", "lost", "won", "draw", "efficiency")
    search_fields = ("user__email", "user__first_name", "user__last_name")
    list_filter = ("country",)

admin.site.register(User, CustomUserAdmin)
