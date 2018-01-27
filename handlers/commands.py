# -*- coding: utf-8 -*-
from coins.prices import get_price_li


def greeting(bot, update):
    """
    deal with start commands

    :param bot:
    :param update:
    :return:
    """
    bot.send_message(chat_id=update.message.chat_id, text="I'm a bot, my name is prekiller!")


def coins(bot, update):
    """
    deal with start commands

    :param bot:
    :param update:
    :return:
    """
    html_text = u"------------\n"
    for coin, price, percent in get_price_li():
        html_text += u"type: {0}, price: {1}, percent: {2}\n".format(coin, price, percent)
    html_text += u"------------\n"
    bot.send_message(chat_id=update.message.chat_id, text=html_text)
