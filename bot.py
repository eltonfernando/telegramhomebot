#!/usr/bin/env python
# pylint: disable=C0116,W0613
# This program is dedicated to the public domain under the CC0 license.

"""
Simple Bot to reply to Telegram messages.

First, a few handler functions are defined. Then, those functions are passed to
the Dispatcher and registered at their respective places.
Then, the bot is started and runs until we press Ctrl-C on the command line.

Usage:
Basic Echobot example, repeats messages.
Press Ctrl-C on the command line or send a signal to the process to stop the
bot.
"""

import logging

from telegram import Update, ForceReply
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
import os
# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)

TOKEN=open('token',"r").read()
# Define a few command handlers. These usually take the two arguments update and
# context.
def read_img():
    path="imagem_evento/movimento.jpg"
    if os.path.isfile(path):
        img_str=open(path,"rb")
        os.remove(path)
    else:
        return ""
    return img_str
def evento_img(context):
    chat_id=context.job.context
    binario=""
    binario=read_img()
    if binario=="":
        print("sem evento")
    else:
        context.bot.send_photo(chat_id,photo=binario)


def start(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /start is issued."""
    context.job_queue.run_repeating(evento_img,interval=10,first=1,context=update.message.chat_id)
    user = update.effective_user
    update.message.reply_markdown_v2(
        fr'Hi {user.mention_markdown_v2()}\!',
        reply_markup=ForceReply(selective=True),
    )


def help_command(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /help is issued."""
    update.message.reply_text('Help!')


def echo(update: Update, context: CallbackContext) -> None:
    """Echo the user message."""
    update.message.reply_text(update.message.text)


def main() -> None:
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    updater = Updater(TOKEN)

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # on different commands - answer in Telegram
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_command))

    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))


    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    main()