"""Admin for matches app"""

#django
from django.db import models
from django.contrib import admin
#model
from cride.matches.models import Match, Request

@admin.register(Request)
class RequestAdmin(admin.ModelAdmin):
  list_display= (
    "back_user",
    "event",
    "back_team",
    "is_matched",
    "amount",
    "is_public"
  )

  search_fields = ("event",)
  list_filter = (
   "is_matched",
  )


@admin.register(Match)
class RequestMatch(admin.ModelAdmin):
  list_display= (
    "event",
    "amount",
    "back_user",
    "back_team",
    "lay_user",
    "lay_team",

  )

  search_fields = ("event",)
