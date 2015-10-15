
import requests
import telebot
import time


token = '125846015:AAFgMHVQuppvHqW-WnZ-A9wYJMa7kxsTGSo'
language = 'ru'
time_for_quote = 60
command = "/start, /help, /stop, /time, /lang"
switcher = True


def listener(messages):


    global switcher
    for m in messages:
        if m.content_type == 'text':

                if m.text.startswith('/help'):

                    bot.send_message(m.chat.id,"Hello my friends, you can command me by next messages: "+command)
                elif m.text.startswith('/start'):
                    switcher = True
                    while switcher:
                          bot.send_message(m.chat.id,get_quote())
                          time.sleep(time_for_quote)
                elif m.text.startswith('/stop'):
                    switcher = False

#Return quote from api.forismatic.com
def get_quote():


    req = requests.get("http://api.forismatic.com/api/1.0/?method=getQuote&format=text&lang="+language)
    return req.text



if __name__ == '__main__':
#Put you token here
    bot  = telebot.TeleBot(token)

    bot.set_update_listener(listener)


# Run for Long Polling. Server holds the request open until new data is available

    bot.polling(none_stop=True)

    while True:
        time.sleep(1)


