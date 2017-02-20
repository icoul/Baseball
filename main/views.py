from django.shortcuts import render
from data.models import PlayerInfo, BetterStat, PitcherStat


def index(request):
    player_info = PlayerInfo.objects.all()
    positions = ['외야수', '내야수', '포수', '투수']
    infos = []
    for player in player_info:
        info = {}
        if player.betterstat_set.values('id'):
            info['player'] = player
            info['stat'] = 1
        elif player.pitcherstat_set.values('id'):
            info['player'] = player
            info['stat'] = 1
        else:
            info['player'] = player
            info['stat'] = None
        infos.append(info)

    return render(request, 'main/index.html', {'infos': infos, 'positions': positions})


def stat(request, pk):
    player_info = PlayerInfo.objects.get(pk=pk)
    if player_info.position == '내야수' or player_info.position == '외야수' or player_info.position == '포수':
        player_stat = BetterStat.objects.get(player_info_id=pk)
    if player_info.position == '투수':
        player_stat = PitcherStat.objects.get(player_info_id=pk)

    return render(request, 'main/stat.html', {'player_info': player_info, 'player_stat': player_stat})
