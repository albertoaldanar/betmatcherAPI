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


@admin.register(Match)
class RequestMatch(admin.ModelAdmin):
  list_display= (
    "request",
    "is_finished",
    "amount",
    "lay_user",
    "lay_team",
    "back_user",
    "back_team"
  )

  search_fields = ("event",)
