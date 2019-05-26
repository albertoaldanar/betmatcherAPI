
#django
from django.db import models
from django.contrib import admin
#model
from cride.events.models import Sport, League, Team, Event

@admin.register(Sport)
class SportAdmin(admin.ModelAdmin):
  list_display= (
    "name",
    "show",
    "icon"
  )
  search_fields = ("name",)

@admin.register(League)
class LeagueAdmin(admin.ModelAdmin):
  list_display= (
    "name",
    "sport",
    "show",
    "order"
  )
  search_fields = ("name",)

  list_filter = (
   "sport",
  )


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
  list_display= (
    "name",
    "league"
  )
  search_fields = ("name",)


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
  list_display= (
    "top_event",
    "league","sport",
    "local","visit",
    "date", "traded"
  )
  search_fields = ("top_event", "league")
