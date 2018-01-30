# -*- coding: utf-8 -*-


from telegram.ext import CommandHandler

from handlers.commands import greeting, coins
from handlers.errors import error_handler

start_handler = CommandHandler('greeting', greeting)
coin_handler = CommandHandler("coins", coins)
