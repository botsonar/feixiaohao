# -*- coding: utf-8 -*-


import logging
import signal
import sys

from telegram.ext import Updater

from handlers import start_handler, coin_handler

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)


def main():
    """
    Create a telegram bot

    :return:
    """

    updater = Updater(token='538103918:AAHhhgULSMKLFcYtR9HDeNDPHlB0MthlLJg')
    dispatcher = updater.dispatcher
    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(coin_handler)

    def stop(signal, frame):
        updater.stop()
        sys.exit(0)

    signal.signal(signal.SIGINT, stop)
    updater.start_polling(poll_interval=1.0)


if __name__ == "__main__":
    main()
