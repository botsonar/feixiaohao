# -*- coding: utf-8 -*-


import logging

from telegram.ext import Updater

from handlers import start_handler, coin_handler, error_handler

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)


def main():
    """
    Create a telegram bot

    :return:
    """

    updater = Updater(
        token='883833096:AAGv377Ng3f427hjJZzdY2XXaFSkDUfmNdk',
    )
    dispatcher = updater.dispatcher
    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(coin_handler)
    dispatcher.add_error_handler(error_handler)

    updater.start_polling(poll_interval=1.0)
    updater.idle()


if __name__ == "__main__":
    main()
