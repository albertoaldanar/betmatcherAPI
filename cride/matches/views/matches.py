"""Events API views"""
#DRF
from rest_framework.views import APIView
from rest_framework import status
from rest_framework import viewsets, mixins
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.decorators import api_view
from rest_framework.decorators import action
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from itertools import chain
#Django
from django.db.models import Q
#Serializer
from cride.matches.serializers import RequestModelSerializer, MatchModelSerializer
from cride.users.serializers import UserModelSerializer
#Models
from cride.matches.models import Request, Match
from cride.users.models import User
from cride.events.models import Event


@api_view(["GET"])
def matches(request):

      permission_classes = (IsAuthenticated,)

      unmatched_bets = Request.objects.filter(
        is_matched = False,
        back_user = request.user
      ).order_by("created")

      matches = Match.objects.filter(Q(back_user = request.user) | Q(lay_user = request.user)).order_by("created")

      matched_bets = matches.filter(is_finished = False)
      finished_bets = matches.filter(event__is_finished = True)

      data = {
        "unmatched_bets": RequestModelSerializer(unmatched_bets, many= True).data,
        "matched_bets": MatchModelSerializer(matched_bets, many= True).data,
        "finished_bets": MatchModelSerializer(finished_bets, many= True).data,
      }

      return Response(data)


@api_view(["POST"])
def post_match(request):
      back_user = User.objects.get(username = request.data["back_user"])
      lay_user = User.objects.get(username = request.data["lay_user"])
      event = Event.objects.get(name = request.data["event"])
      req = Request.objects.get(id = request.data["request"])

      response = Match.objects.create(
        back_user = back_user,
        lay_user = lay_user,
        amount = request.data["amount"],
        back_team = request.data["back_team"],
        lay_team = request.data["lay_team"],
        event = event,
        request = req
      )

      data = {"match": MatchModelSerializer(response).data}

      req.is_matched = True
      req.save()

      event.traded += int(request.data["amount"])
      event.unmatched_bets -=1
      event.matched_bets +=1
      event.save()

      return Response(data)


@api_view(["PUT"])
def finish_match(request):
      match = Match.objects.get(id = request.data["match"])
      event = match.event
      back_user = match.back_user.profile
      lay_user = match.lay_user.profile

      event.is_finished = True
      event.save()


      data = {"match": MatchModelSerializer(match).data}

      def save_users(user_a, user_b):
        user_a.save()
        user_b.save()

      def stats_and_pay(winOrBack, loseOrLay, draw):
        if draw:
            winOrBack.coins += (match.amount / 2)
            loseOrLay.coins += (match.amount / 2)
            winOrBack.draw += 1
            loseOrLay.draw += 1
            save_users(winOrBack, loseOrLay)
        else:
            winOrBack.coins += match.amount
            winOrBack.won += 1
            loseOrLay.lost += 1
            save_users(winOrBack, loseOrLay)

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
                analyse_score(None, match.back_user, match.lay_user)

            elif match.back_team == "Draw" and match.lay_team == event.visit.name:
                analyse_score(None, match.lay_user, match.back_user)


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

      return Response(data)
