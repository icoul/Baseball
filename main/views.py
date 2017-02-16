from django.shortcuts import render
from data.models import PlayerInfo, BetterStat, PitcherStat


def index(request):
    player_info = PlayerInfo.objects.all()
    infos = []
    for player in player_info:
        info = {}
        if player.betterstat_set.all():
            info['player'] = player
            info['stat'] = player.betterstat_set.all()
        elif player.pitcherstat_set.all():
            info['player'] = player
            info['stat'] = player.pitcherstat_set.all()
        else:
            info['player'] = player
            info['stat'] = None
        infos.append(info)

    return render(request, 'main/index.html', {'infos': infos})
