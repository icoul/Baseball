from django.shortcuts import render
from bs4 import BeautifulSoup
from .models import Data
import urllib.request
import re


def soup_data(url):
    req = urllib.request.Request(url)
    data = urllib.request.urlopen(req).read()
    soup = BeautifulSoup(data, 'html.parser')

    return soup

def data(request):
    soup = soup_data('http://www.samsunglions.com/roster/roster_3_list.asp')
    urls = []
    for x in soup.find_all('a'):
        if re.search(r'[0-9]+$', x.get('href')):
            urls.append(x.get('href').split('=')[1])

    for number in urls:
        player = []
        url = 'http://www.samsunglions.com/roster/roster_2.asp?pcode=' + number
        soup = soup_data(url)
        for x in soup.find('strong', ['t']):
            if not x.string:
                player.append(0)
            else:
                player.append(x.string.strip())

        position = soup.find('em', ['s']).string.split('/')
        position = position[0]
        hand = position[1].strip()

        for x in soup.find('p'):
            if not x.string:
                continue

            info = x.strip().split(' : ')

            if x.string and info[0] == '생년월일':
                birth = re.findall(r'[0-9]+', info[1])
                birth = birth[0] + '-' + birth[1] + '-' + birth[2]
                continue
            if x.string and info[0] == '키/몸무게' and re.search(r'[0-9]+', info[1]):
                w_and_h = re.findall(r'[0-9]+', info[1])
                height = w_and_h[0]
                player.append(w_and_h[1])
                break
            else:
                height = 0
                weight = 0
                break

        data_insert = Data(number = player[0], name = player[1], position = position, hand = hand, birth = birth, height = height, weight = weight)
        data_insert.save()
        render(request, 'data/index.html')
