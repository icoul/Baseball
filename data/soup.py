from bs4 import BeautifulSoup
import urllib.request
import re


def soup_data(url):
    req = urllib.request.Request(url)
    data = urllib.request.urlopen(req).read()
    soup = BeautifulSoup(data, 'html.parser')

    return soup

soup = soup_data('http://www.statiz.co.kr/player.php?name=%EC%9C%A4%EC%84%B1%ED%99%98&birth=1981-10-08')
stat_name = ['game', 'complited_game', 'shutout', 'games_started', 'wins', 'loses', 'save', 'hold', 'inning',
             'runs', 'earned_runs', 'batter', 'hits', 'doubles',
             'triples', 'home_runs', 'bases_on_balls', 'intentional_bob', 'hit_by_pitch',
             'strike_out', 'balks', 'wild_pitches', 'era', 'fip', 'whip', 'era_plus', 'fip_plus', 'war', 'wpa']
stat = {}
flag = 0
stat_data = soup.find_all('td', 'statdata')

for x in stat_data:
    if flag == 0 and x.string != '2016':
        break

    flag += 1
    if flag < 2:
        continue
    if x.string == '2016':
        break
    stat[stat_name[flag - 2]] = x.string

print(stat)



