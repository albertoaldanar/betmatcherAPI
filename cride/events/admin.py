
#django
from django.db import models
from django.contrib import admin
#model
from cride.events.models import Sport, League, Team, Event, Banner
from cride.matches.models import Match, Request
import time, threading

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

@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
  list_display= (
    "img",
    "title",
    "message",
  )
  search_fields = ("title",)

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
    "in_play",
    "is_finished",
    "league",
    "local","visit",
    "traded",
    "matched_bets", "unmatched_bets"
  )
  list_filter = (
    "in_play", "is_finished"
  )
  search_fields = ("top_event", "league")

  actions = ["finish_event", "start_clock", "second_time"]


  t =  threading.Timer(1, None)

  def start_clock(self, request, queryset):
    queryset.update(in_play = True)
    WAIT_SECONDS = 10

    for event in queryset:
      def start():
          t =  threading.Timer(WAIT_SECONDS, start)

          if event.minute == 45:
            event.time = "Half time"
            event.save()

            ticker = threading.Event();

          else:
            event.minute += 1
            event.save()
            print(event.minute)
            t.start()
      start()

  def second_time(self, request, queryset, *args, **kwds):
    queryset.update(in_play = True, minute = 45)
    WAIT_SECONDS = 60

    for event in queryset:
      def start():
        t =  threading.Timer(WAIT_SECONDS, start)

        if event.minute == 90: 
          t.cancel()

        else:
          event.time = ""
          event.half_time = False
          event.minute += 1
          event.save()

        print(event.minute)
        t.start()

      start()


  def finish_event(self, request, queryset):
    queryset.update(is_finished = True, in_play = False)
 

    def return_unmatched(req):
        for r in req:
          unmatched_user = r.back_user.profile
          unmatched_user.coins += r.amount
          unmatched_user.save()


    def payment(matches, req, event):

      for m in matches:  

          return_unmatched(req)

          back_user = m.back_user.profile
          lay_user = m.lay_user.profile

          def save_users(user_a, user_b, m):
            user_a.save()
            user_b.save()
            m.save()

          def stats_and_pay(winOrBack, loseOrLay, draw):
            if draw:
                if m.quote > 0:
                    add_quote = [m.request.amount, (m.request.amount - m.quote)] if winOrBack.username == m.back_user.username else [(m.request.amount - m.quote), m.request.amount]

                    winOrBack.coins += add_quote[0]
                    loseOrLay.coins += add_quote[1]
                    winOrBack.draw += 1
                    loseOrLay.draw += 1
                    m.draw = True
                    save_users(winOrBack, loseOrLay, m)
                else:
                    add_quote = [(m.request.amount + (m.quote * -1)), m.request.amount] if loseOrLay.username == m.lay_user.username else [m.request.amount, (m.request.amount + (m.quote * -1))]

                    winOrBack.coins += add_quote[1]
                    loseOrLay.coins += add_quote[0]
                    winOrBack.draw += 1
                    loseOrLay.draw += 1
                    m.draw = True
                    save_users(winOrBack, loseOrLay, m)
            else:
                winOrBack.coins += m.amount
                winOrBack.won += 1
                loseOrLay.lost += 1
                m.winner = winOrBack.username
                m.looser = loseOrLay.username
                save_users(winOrBack, loseOrLay, m)

          def get_relation():
              #local vs visit
              if m.back_team == event.local.name and m.lay_team == event.visit.name:
                  analyse_score(back_user, lay_user, None)
              elif m.back_team == event.visit.name and m.lay_team == event.local.name:
                  analyse_score(lay_user, back_user, None)

              #local vs draw
              elif m.back_team == event.local.name and m.lay_team == "Draw":
                  analyse_score(back_user, None, lay_user)
              elif m.back_team == "Draw" and m.lay_team == event.local.name:
                  analyse_score(lay_user, None, back_user)

              #visit vs draw
              elif m.back_team == event.visit.name and m.lay_team == "Draw":
                  analyse_score(None, back_user, lay_user)

              elif m.back_team == "Draw" and m.lay_team == event.visit.name:
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
        second_time("end")

        req = Request.objects.filter(event__id = event.id, is_matched = False)

        try:
          matches = Match.objects.filter(event__id = event.id)
        except Match.DoesNotExist:
          matches = None

        if matches:
            payment(matches, req, event)
        else:
            return_unmatched(req)


