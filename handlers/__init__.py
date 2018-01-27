# -*- coding: utf-8 -*-


from telegram.ext import CommandHandler

from handlers.commands import greeting, coins

start_handler = CommandHandler('greeting', greeting)
coin_handler = CommandHandler("coins", coins)
