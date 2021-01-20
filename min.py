from transliterate import to_cyrillic, to_latin
import telebot
from flask import Flask, request
import os
TOKEN='1588108567:AAFzUQVPWPsIhTpu16pAC2LWwRowpxlaz1A'
bot = telebot.TeleBot(TOKEN, parse_mode=None) # You can set parse_mode by default. HTML or MARKDOWN

@bot.message_handler(commands=['start'])
def send_welcome(message):
        javob="Assalomu alekum, Hush kelibsiz!\nUshbu bot matnlarni lotin alifbosidan kiril alifbosiga yoki aksincha ogirib bera oladi buning uchun so'zni kiriting\nPowered by @mirabbos"
        bot.reply_to(message, javob)
@bot.message_handler(func=lambda message: True)
def echo_all(message):
        msg=message.text
        javob=lambda msg: to_cyrillic(msg) if msg.isascii() else to_latin(msg)
        bot.reply_to(message, javob(msg))

bot.polling()
##matn=input('Matnni kiriting: ')
##if(matn.isascii()):
##    print(to_cyrillic(matn))
##else:
##    print(to_latin(matn))
@server.route('/' + TOKEN, methods=['POST'])
def getMessage():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "!", 200


@server.route("/")
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url='https://your_heroku_project.com/' + TOKEN)
    return "!", 200


if __name__ == "__main__":
    server.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))