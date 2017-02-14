from django.shortcuts import render
from bs4 import BeautifulSoup
from .models import Player_info
from .models import Better_stat, Pitcher_stat
import urllib.request
import re


def soup_data(url):
    req = urllib.request.Request(url)
    data = urllib.request.urlopen(req).read()
    soup = BeautifulSoup(data, 'html.parser')

    return soup


def player_data(url_number):
    player = []
    url = 'http://www.samsunglions.com/roster/roster_2.asp?pcode=' + url_number
    soup = soup_data(url)
    for x in soup.find('strong', ['t']):
        if not x.string:
            player.append(0)
        else:
            player.append(x.string.strip())

    position_hand = soup.find('em', ['s']).string.split('/')
    player.append(position_hand[0])
    player.append(position_hand[1].strip())

    for x in soup.find('p'):
        if not x.string:
            continue

        info = x.strip().split(' : ')

        if x.string and info[0] == '생년월일':
            birth = re.findall(r'[0-9]+', info[1])
            player.append(birth[0] + '-' + birth[1] + '-' + birth[2])
            continue
        if x.string and info[0] == '키/몸무게' and re.search(r'[0-9]+', info[1]):
            w_and_h = re.findall(r'[0-9]+', info[1])
            player.append(w_and_h[0])
            player.append(w_and_h[1])
            break
        else:
            player.append(0)
            player.append(0)
            break

    return player


def batter(request):
    soup = soup_data('http://www.samsunglions.com/roster/roster_3_list.asp')
    urls = []
    for x in soup.find_all('a'):
        if re.search(r'[0-9]+$', x.get('href')):
            urls.append(x.get('href').split('=')[1])

    for url_number in urls:
        player = player_data(url_number)

        data_insert = Player_info(number=player[0], name=player[1], position=player[2], hand=player[3], birth=player[4],
                                  height=player[5], weight=player[6])
        data_insert.save()

    return render(request, 'data/batter.html')


def pitcher(request):
    soup = soup_data('http://www.samsunglions.com/roster/roster_2_list.asp')
    urls = []
    for x in soup.find_all('a'):
        if re.search(r'[0-9]+$', x.get('href')):
            urls.append(x.get('href').split('=')[1])

    for url_number in urls:
        player = player_data(url_number)

        data_insert = Player_info(number=player[0], name=player[1], position=player[2], hand=player[3], birth=player[4],
                                  height=player[5], weight=player[6])
        data_insert.save()

    return render(request, 'data/pitcher.html')


def batter_stat(request):
    positions = ['내야수', '외야수', '포수']
    info = Player_info.objects.filter(position__in = positions)

    stat_name = ['all_bats', 'at_bats', 'runs_scored', 'hits', 'doubles', 'triples', 'home_runs', 'total_base',
                 'runs_batted_in', 'stolen_bases', 'caught_stealing', 'bases_on_balls', 'hit_by_pitch',
                 'intentional_bob', 'strike_out', 'double_play', 'sacrifice', 'sacrifice_fly',
                 'batting_avg', 'on_base_per', 'slugging_per', 'ops', 'woba', 'wrc_plus', 'war', 'wpa']

    for member in info:
        name = str(member.name.encode('utf-8'))[2:-1]
        utf_name = name.replace(name[0:2], '%').upper()

        url = 'http://www.statiz.co.kr/player.php?name=' + utf_name + '&birth=' + member.birth
        soup = soup_data(url)
        stat = {}
        flag = 0
        stat_data = soup.find_all('td', 'statdata')

        if not stat_data:
            continue

        for x in stat_data:
            if flag == 0 and x.string != '2016':
                break

            flag += 1
            if flag < 3:
                continue
            if x.string == '2016':
                break
            stat[stat_name[flag - 3]] = x.string

        if not stat:
            continue

        stat_insert = Better_stat(name=member.name, player_info_id=member.id, all_bats=stat['all_bats'],
                                  at_bats=stat['at_bats'], runs_scored=stat['runs_scored'], hits=stat['hits'],
                                  doubles=stat['doubles'], triples=stat['triples'], home_runs=stat['home_runs'],
                                  total_base=stat['total_base'], runs_batted_in=stat['runs_batted_in'],
                                  stolen_bases=stat['stolen_bases'], caught_stealing=stat['caught_stealing'],
                                  bases_on_balls=stat['bases_on_balls'], hit_by_pitch=stat['hit_by_pitch'],
                                  intentional_bob=stat['intentional_bob'], strike_out=stat['strike_out'],
                                  double_play=stat['double_play'], sacrifice=stat['sacrifice'],
                                  sacrifice_fly=stat['sacrifice_fly'], batting_avg=stat['batting_avg'],
                                  on_base_per=stat['on_base_per'], slugging_per=stat['slugging_per'],
                                  ops=stat['ops'], woba=stat['woba'], wrc_plus=stat['wrc_plus'], war=stat['war'],
                                  wpa=stat['wpa'])
        stat_insert.save()

    return render(request, 'data/batter_stat.html')


def pitcher_stat(request):
    info = Player_info.objects.filter(position = '투수')

    stat_name = ['game', 'complited_game', 'shutout', 'games_started', 'wins', 'loses', 'save', 'hold', 'inning',
                 'runs', 'earned_runs', 'batter', 'hits', 'doubles',
                 'triples', 'home_runs', 'bases_on_balls', 'intentional_bob', 'hit_by_pitch',
                 'strike_out', 'balks', 'wild_pitches', 'era', 'fip', 'whip', 'era_plus', 'fip_plus', 'war', 'wpa']

    for member in info:
        name = str(member.name.encode('utf-8'))[2:-1]
        utf_name = name.replace(name[0:2], '%').upper()

        url = 'http://www.statiz.co.kr/player.php?name=' + utf_name + '&birth=' + member.birth
        soup = soup_data(url)
        stat = {}
        flag = 0
        stat_data = soup.find_all('td', 'statdata')

        if not stat_data:
            continue

        for x in stat_data:
            if flag == 0 and x.string != '2016':
                break

            flag += 1
            if flag < 2:
                continue
            if x.string == '2016':
                break
            stat[stat_name[flag - 2]] = x.string

        if not stat:
            continue

        stat_insert = Pitcher_stat(name=member.name, player_info_id=member.id, game=stat['game'],
                                  complited_game=stat['complited_game'], shutout=stat['shutout'], games_started=stat['games_started'],
                                  wins=stat['wins'], loses=stat['loses'], save=stat['save'],
                                  hold=stat['hold'], inning=stat['inning'],
                                  runs=stat['runs'], earned_runs=stat['earned_runs'],
                                  batter=stat['batter'], hits=stat['hits'],
                                  doubles=stat['doubles'], triples=stat['triples'],
                                  home_runs=stat['home_runs'], bases_on_balls=stat['bases_on_balls'],
                                  intentional_bob=stat['intentional_bob'], hit_by_pitch=stat['hit_by_pitch'],
                                  strike_out=stat['strike_out'], balks=stat['balks'],
                                  wild_pitches=stat['wild_pitches'], era=stat['era'], fip=stat['fip'], whip=stat['whip'],
                                  era_plus=stat['era_plus'], fip_plus=stat['fip_plus'], war=stat['war'], wpa=stat['wpa'])
        stat_insert.save()

    return render(request, 'data/pitcher_stat.html')

