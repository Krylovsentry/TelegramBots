
import requests
import telebot
import time


token = ''
language = 'en'



def listener(messages):


    for m in messages:

        if m.content_type == 'text':
            quote_every_hour(messages,True)






def quote_every_hour(messages,switcher):

  while switcher:
           for m in messages:

               bot.send_message(m.chat.id,get_quote())
               #time.sleep make a pause in executing script, on a value of second that we write in the field
               time.sleep(5)





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
        time.sleep(200)


