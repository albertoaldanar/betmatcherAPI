
#django
from django.db import models
from django.contrib import admin
#model
from cride.events.models import Sport, League, Team, Event
from cride.matches.models import Match, Request

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
    "is_finished",
    "league",
    "local","visit",
    "date", "traded",
    "matched_bets", "unmatched_bets"
  )
  list_filter = (
    "top_event",
  )
  search_fields = ("top_event", "league")

  actions = ["finish_event"]

  def finish_event(self, request, queryset):
    queryset.update(is_finished = True, in_play = False)


    def return_unmatched(req):
        for r in req:
          unmatched_user = r.back_user.profile
          unmatched_user.coins += r.amount
          unmatched_user.save()


    def payment(match, req, event):

          return_unmatched(req)

          back_user = match.back_user.profile
          lay_user = match.lay_user.profile

          def save_users(user_a, user_b, match):
            user_a.save()
            user_b.save()
            match.save()

          def stats_and_pay(winOrBack, loseOrLay, draw):
            if draw:
                winOrBack.coins += (match.amount / 2)
                loseOrLay.coins += (match.amount / 2)
                winOrBack.draw += 1
                loseOrLay.draw += 1
                match.draw = True
                save_users(winOrBack, loseOrLay, match)
            else:
                winOrBack.coins += match.amount
                winOrBack.won += 1
                loseOrLay.lost += 1
                match.winner = winOrBack.username
                match.looser = loseOrLay.username
                save_users(winOrBack, loseOrLay, match)

          def get_relation():
              #local vs visit
              if match.back_team == event.local.name and match.lay_team == event.visit.name:
                  analyse_score(back_user, lay_user, None)
              elif match.back_team == event.visit.name and match.lay_team == event.local.name:
                  analyse_score(lay_user, back_user, None)

              #local vs draw
              elif match.back_team == event.local.name and match.lay_team == "Draw":
                  analyse_score(back_user, None, lay_user)
              elif match.back_team == "Draw" and match.lay_team == event.local.name:
                  analyse_score(lay_user, None, back_user)

              #visit vs draw
              elif match.back_team == event.visit.name and match.lay_team == "Draw":
                  analyse_score(None, back_user, lay_user)

              elif match.back_team == "Draw" and match.lay_team == event.visit.name:
                  analyse_score(None, lay_user, back_user)


          def analyse_score(local, visit, draw):
            score_local = event.score_local
            score_visit = event.score_visit
            #Local
            if score_local > score_visit:
                if local == None:
                  stats_and_pay(draw, visit, True)
                elif local!= None and visit == None:
                  stats_and_pay(local, draw, False)
                elif local!= None and draw == None:
                  stats_and_pay(local, visit, False)

            #Visit
            elif score_local < score_visit:
                if visit == None:
                  stats_and_pay(local, draw, True)
                elif visit!= None and local == None:
                  stats_and_pay(visit, draw, False)
                elif local!= None and draw == None:
                  stats_and_pay(visit, local, False)
            #Draw
            else:
                if draw == None:
                  stats_and_pay(local, visit, True)
                elif draw!= None and visit == None:
                  stats_and_pay(draw, local, False)
                elif draw!= None and local == None:
                  stats_and_pay(draw, visit, False)

          get_relation()

    for event in queryset:
        req = Request.objects.filter(event__id = event.id, is_matched = False)

        try:
          match = Match.objects.get(event__id = event.id)
        except Match.DoesNotExist:
          match = None

        if match:
            payment(match, req, event)
        else:
            return_unmatched(req)


