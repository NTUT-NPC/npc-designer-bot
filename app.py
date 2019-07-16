import random, os
from telegram.ext import Updater, CommandHandler
import logging


if os.path.exists('sentences.txt'):
    with open('sentences.txt') as FILE:
        sentences = [sentence.strip() for sentence in FILE]
else:
    sentences = []

def add(bot, update):
    print('from user:', update.message.from_user.id)
    if True:
        sentence = update.message.text[5:].replace('\n', ' ')
        sentences.append(sentence)
        with open('sentences.txt', 'a') as FILE:
            print(sentence, file=FILE)
        update.message.reply_text('已加入：' + sentence)

def say(bot, update):
    if sentences:
        update.message.reply_text(random.choice(sentences))
    else:
        update.message.reply_text('I have no words.')


updater = Updater('802581448:AAHSo3ksANNddPYeSWh6WnZ1Gt5hfNeWF7E')

updater.dispatcher.add_handler(CommandHandler('add', add))
updater.dispatcher.add_handler(CommandHandler('say', say))

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)
updater.start_polling()
updater.idle()