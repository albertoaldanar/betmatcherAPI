"""User models admin"""

#Django
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

#Models
from cride.users.models import User, Profile, Prize, Exchange


class CustomUserAdmin(UserAdmin):
  """User admin"""

  list_display = ("email", "username", "id", "first_name", "country")
  list_filter = ("created", "modified", "username")


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("username", "won", "draw", "lost", "coins")
    search_fields = ("user__email", "user__first_name", "user__last_name")
    list_filter = ("country",)



@admin.register(Prize)
class PrizeAdmin(admin.ModelAdmin):
  list_display= (
    "name", "description",
    "price"
  )

@admin.register(Exchange)
class ExchangeAdmin(admin.ModelAdmin):
  list_display= (
    "user", "prize", "date"
  )


admin.site.register(User, CustomUserAdmin)
