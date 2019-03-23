# -*- coding: utf-8 -*-

from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import as_completed

from requests_html import HTMLSession
session = HTMLSession()


coins = [
    "cybermiles",
    "decent"
]


def get_price(coin_type):
    result = session.get("https://www.feixiaohao.com/currencies/{0}/".format(coin_type), verify=False, timeout=3)
    if result:
        return (coin_type, result.html.find(".val.textGreen")[0].text, result.html.find("div.sub.smallfont > span:nth-child(1)")[0].text)
    return None


def get_price_li():
    executor = ThreadPoolExecutor(10)
    futures = [executor.submit(get_price, coin) for coin in coins]
    prices = []
    for r in as_completed(futures):
        if r.result():
            prices.append(r.result())
    return prices


if __name__ == "__main__":
    print(get_price_li())
