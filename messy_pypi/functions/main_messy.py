import math
import os
import subprocess
import urllib.parse as urlparse
from typing import Generator
from urllib.parse import parse_qs
from urllib.parse import urlencode

import requests
from bs4 import BeautifulSoup

os.chdir('..')
from classes.main_messy import List


def human_delta_time(time: int, currentValue: str = 'seconde', minValue: str = 'seconde', maxValue: str = 'jour',
                     remove: list = None) -> str:
    word = List(['seconde', 'minute', 'heure', 'jour', 'mois', 'année'])
    if remove: word.rmMALL(remove)


def split_every_n(seq: any, n: int) -> Generator:
    while seq:
        yield seq[:n]
        seq = seq[n:]


def split(seq, every: int = None, by: any = None) -> list:
    if every:
        return list(split_every_n(seq, every))
    elif by:
        return seq.split(seq, by)


def show_wifi_pwd() -> None:
    data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('850').split('\n')
    profiles = [i.split(":")[1][1:-1] for i in data if
                ("All User Profile" in i) or ("Profil Tous les utilisateurs" in i)]
    for i in profiles:
        results = subprocess.check_output('netsh wlan show profile "' + i + '" key=clear').decode('850').split('\n')
        results = [b.split(":")[1][1:-1] for b in results if ("Key Content" in b) or ('Contenu de la clé' in b)]
        try:
            print("{:<30}|  {:<}".format(i, results[0]))
        except IndexError:
            print("{:<30}|  {:<}".format(i, ""))


def human_number_word(n: (int or float)) -> str:
    millnames = ['', ' Mille', ' Million', ' Milliard',
                 ' Billion', ' Billiard', ' Trillion',
                 ' Trilliard', ' Quadrillion', ' Quadrilliard',
                 ' Quintillion', ' Quintilliard', ' Sextillion',
                 ' Sextilliard', ' Septillion', ' Septilliard',
                 ' Octillion', ' Octilliard', ' Nonillion',
                 ' Nonilliard', ' Decillion', ' Decilliard']
    n = float(n)
    millidx = max(0, min(len(millnames) - 1, int(math.floor(0 if n == 0 else math.log10(abs(n)) / 3))))
    return '{:.0f}{}'.format(n / 10 ** (3 * millidx), millnames[millidx])


def human_hours(seconds: int) -> None:
    a = str(seconds // 3600)
    b = str((seconds % 3600) // 60)
    c = str((seconds % 3600) % 60)
    d = ["{} hours {} mins {} seconds".format(a.zfill(2), b.zfill(2), c.zfill(2))]
    print(d)


def escape_string(name: str) -> str:
    return name.rstrip().lstrip().strip()


def get_html(link: str) -> BeautifulSoup:
    html = requests.request("GET", link, headers={}, data={}).text.encode("utf8")
    return BeautifulSoup(html, "html.parser")


def url_parse(link: str) -> dict:
    parsed = urlparse.urlparse(link)
    return parse_qs(parsed.query)


def url_make(url: str, params: dict) -> str:
    url_parts = list(urlparse.urlparse(url))
    query = dict(urlparse.parse_qsl(url_parts[4]))
    query.update(params)
    url_parts[4] = urlencode(query)
    return urlparse.urlunparse(url_parts)


def pypi_search(query: str, page: int = 1, printv: bool = True, returnv: bool = False) -> None:
    if returnv: printv = False
    link = url_make('https://pypi.org/search/', {'q': query, 'page': page})
    root = get_html(link)
    if not root: return
    pt = root.find('ul', {'aria-label': 'Search results'})
    if not pt: return
    pr = pt.findAll('li')
    if not pr: return
    name = List()
    url = List()
    for i in pr:
        name.append(i.find("span", {"class": "package-snippet__name"}).text)
        url.append(i.find("a", {"class": "package-snippet"})['href'])
    for n, u in zip(name, url):
        if printv:
            print(f"{n} {' ' * (len(name.maxl) - len(n) + 2)} | https://pypi.org{u}")
    btn = root.find('div', {'class': 'button-group--pagination'})
    if btn:
        btn = btn.findAll('a')
        btn = List(map(lambda x: x.text if x.text.isnumeric() else None, btn))
        btn.clearNotValue()
        btn.toType()
        if printv:
            print(f"{url_parse(link)['page'][0]}/{max(btn.maxv, url_parse(link)['page'][0])}")
        else:
            return [{"page": url_parse(link)['page'][0], "query": url_parse(link)['q'][0]}] + zip(name, url)
    return [{"page": url_parse(link)['page'][0], "query": url_parse(link)['q'][0]}]
