# Databricks notebook source
import pip
import requests


import requests
from bs4 import BeautifulSoup
import html

cookies = {
            '_ALGOLIA': '1ff3e68a-e8b4-4a6f-8e56-8f290000f1bd',
            'ut_d_l': '85e6a097998ee6508550773a6cf84700dfa32a05beb09d10d32a608a89cd21e50f93ce8daf3fb9e71b3893bc162b94bc082b44e8afdedf840df11210e4115807wUw7FPV0%2FiM7yKwCd6wB7dpGUTON0Cb8OaCghMunA9alHhga4KONvLAHaZEHJXPoEyr89lYn3PvJhTq%2FJ%2FDa8Q%3D%3D',
            'untappd_user_v3_e': '63841460c38af68797cd1d3f5492a9efbe115c96b588b8e6f8e4e2a27415654b301f75ea530df2455d8a9188ceeaddfd2889eb5fe0163cb048fba2f091233491euzSn47l7GKjDPJuu1ZESK%2Bt%2FhKprd5eM8LBK0CT%2BUdQAqDSrb12MZlaoK0hCbiNChj53qmie%2BWxgblUfgzL4g%3D%3D',
            'untappd_session_t': 'YTNnbmJFY0xOTUJXUTR2Qy15STFUNGhrc2R2RG9FZTM1R0dzK3pnPT0%3D',
            'ut_tos_update': 'true',
            'untappd_traits': '4516951',
        }

headers = {
    'authority': 'untappd.com',
    'accept': '*/*',
    'accept-language': 'en-GB,en;q=0.9',
    # 'cookie': '_ALGOLIA=1ff3e68a-e8b4-4a6f-8e56-8f290000f1bd; ut_d_l=85e6a097998ee6508550773a6cf84700dfa32a05beb09d10d32a608a89cd21e50f93ce8daf3fb9e71b3893bc162b94bc082b44e8afdedf840df11210e4115807wUw7FPV0%2FiM7yKwCd6wB7dpGUTON0Cb8OaCghMunA9alHhga4KONvLAHaZEHJXPoEyr89lYn3PvJhTq%2FJ%2FDa8Q%3D%3D; untappd_user_v3_e=63841460c38af68797cd1d3f5492a9efbe115c96b588b8e6f8e4e2a27415654b301f75ea530df2455d8a9188ceeaddfd2889eb5fe0163cb048fba2f091233491euzSn47l7GKjDPJuu1ZESK%2Bt%2FhKprd5eM8LBK0CT%2BUdQAqDSrb12MZlaoK0hCbiNChj53qmie%2BWxgblUfgzL4g%3D%3D; untappd_session_t=YTNnbmJFY0xOTUJXUTR2Qy15STFUNGhrc2R2RG9FZTM1R0dzK3pnPT0%3D; ut_tos_update=true; untappd_traits=4516951',
    'referer': 'https://untappd.com/search?q=beer&type=beer&sort=all',
    'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Brave";v="110"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'sec-gpc': '1',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}

beer_dicts = []
params = {
    'offset': 25,
    'q': 'beer',
    'sort': 'all',
}

offset = 0
while True:
    offset = offset + 25
    params = {
        'offset': offset,
        'q': 'beer',
        'sort': 'all',
    }
    response = requests.get('https://untappd.com/search/more_search/beer', params=params, cookies=cookies, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    beers = soup.findAll('div', attrs={'class': 'beer-item'})
    if len(beers) == 0:
        print(len(beers))
        break
    else:
        print(len(beers))
    for beer in beers:
        beer_details = beer.find('div', attrs={'class': 'beer-details'})
        details_beer = beer.find('div', attrs={'class': 'details beer'})
        beer_details_paragraphs = beer_details.findAll('p')
        beer_name = html.unescape(beer_details_paragraphs[0].text)
        beer_brewery = html.unescape(beer_details_paragraphs[1].text)
        beer_category = html.unescape(beer_details_paragraphs[2].text)
        beer_abv = html.unescape(details_beer.find('p', attrs={'class': 'abv'}).text.replace('\n', ''))
        beer_ibu = html.unescape(details_beer.find('p', attrs={'class': 'ibu'}).text.replace('\n', ''))
        beer_rating = html.unescape(details_beer.find('div', attrs={'class': 'caps'})['data-rating'])
        beer_dict = {
            "name": beer_name,
            "brewery": beer_brewery,
            "category": beer_category,
            "abv": beer_abv,
            "ibu": beer_ibu,
            "rating": beer_rating
        }
        beer_dicts.append(beer_dict)

import json
with open('beers.json', 'w+') as f:
    json.dump(beer_dicts, f)