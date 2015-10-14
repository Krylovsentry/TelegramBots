
import requests
import telebot
import time


language = 'en'


def listener(messages):


    for m in messages:

        if m.content_type == 'text':

            bot.send_message(m.chat.id, get_quote())



def get_quote():


    req = requests.get("http://api.forismatic.com/api/1.0/?method=getQuote&format=text&lang="+language)
    return req.text



if __name__ == '__main__':
#Put you token here
    bot  = telebot.TeleBot()

    bot.set_update_listener(listener)

# Run for Long Polling. Server holds the request open until new data is available

    bot.polling(none_stop=True)

    while True:
        time.sleep(200)


