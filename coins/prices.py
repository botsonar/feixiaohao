# -*- coding: utf-8 -*-


import requests
from bs4 import BeautifulSoup

coins = [
    "bitcoin",
    "raiblocks",
    "iost"
]


def get_price(coin_type):
    """
    Get coin price from feixiaohao

    :param coin_type:
    :return:
    """
    prices = []
    resp = requests.get("https://www.feixiaohao.com/currencies/{0}/".format(coin_type))
    bs = BeautifulSoup(resp.text, "lxml")
    for maket in bs.find_all("div", class_="cell maket"):
        for item in maket.find_all("div", class_="coinprice"):
            prices.append((coin_type, item.next, item.span.text))
    return prices


def get_price_li():
    prices = []
    for coin in coins:
        prices.extend(get_price(coin))
    return prices


if __name__ == "__main__":
    print(get_price_li())
