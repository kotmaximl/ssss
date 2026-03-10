import telebot
from telebot import types
from flask import Flask
import threading
import os

TOKEN = "8446394597:AAHxj-iGglalo2G3mOIL9JWZBFAp5QyU7-g"

bot = telebot.TeleBot(TOKEN)
app = Flask(__name__)


# ===== ФЕЙКОВЫЙ СЕРВЕР ДЛЯ RENDER =====
@app.route("/")
def home():
    return "Bot is alive"


def run_web():
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)


# ===== СПИСОК ФОТО =====
PHOTO_MAP = {
    "Письмо Рейнхарда": "AgACAgIAAxkBAAIDRmmsgLYpeRkE_-WKjrj3BzkTQ8QKAAL8E2sb_jJoSZfvaXnUO6NMAQADAgADeAADOgQ",
    "Доклад айнзацгрупп": "AgACAgIAAxkBAAIDaGmsgm4hvmXk39a9NDkMufBUCH4hAAIPFGsb_jJoSZpKlJ--RA5kAQADAgADbQADOgQ",
    "Доклад Гитлеру о казнях": "AgACAgIAAxkBAAIDaWmsgn9xuLWctmhXuijXX07tlGoVAAIQFGsb_jJoSUckNjR5xw8KAQADAgADeAADOgQ",
    "Население евреев в мире": "AgACAgIAAxkBAAIDammsgo5SQf2U3k8V0pyradAF_VcZAAIRFGsb_jJoSdinz-zZEaJ7AQADAgADeAADOgQ",
    "Отчёт Егера": "AgACAgIAAxkBAAIDaWmsgn9xuLWctmhXuijXX07tlGoVAAIQFGsb_jJoSUckNjR5xw8KAQADAgADeAADOgQ",
    "Отчёт Корхера": "AgACAgIAAxkBAAIDRmmsgLYpeRkE_-WKjrj3BzkTQ8QKAAL8E2sb_jJoSZfvaXnUO6NMAQADAgADeAADOgQ",
    "Отчёт Юргена Штропа": "AgACAgIAAxkBAAIDbWmsgvjrl6R9B8DlG94bQqCiPq8GAAIWFGsb_jJoSS1B9taT8AmWAQADAgADeQADOgQ",
    "Перепись населения Львовского воеводства": "AgACAgIAAxkBAAIDbmmsgwaWc3GIIDV4tyX8-BnaKl05AAIXFGsb_jJoSYycIvqO18LQAQADAgADeQADOgQ",
    "Распоряжение для евреев": "AgACAgIAAxkBAAIDb2msgxk2bXE_ZO7SFpu5G2DcghQvAAIYFGsb_jJoSbRY9s8JMC3sAQADAgADeAADOgQ",
    "Религии в мире": "AgACAgIAAxkBAAIDcGmsgyhWEMyWKul3XJvGEEhHZ4OtAAIaFGsb_jJoSaSgZyFwDqbfAQADAgADeAADOgQ",
    "Еврейское население Европы 1939-1991": "AgACAgIAAxkBAAIDcWmsgzLwVdBm4dt7TqUVC8UviuFWAAIbFGsb_jJoSTKLkf9lRFXQAQADAgADeQADOgQ",
}


# ===== СПИСОК PDF =====
FILE_MAP = {
    "Перепись СССР 1939": "BQACAgIAAxkBAAIDcmmsg0oKx3HbZITML7LQhbuKUK6KAALalAAC_jJoSdtIPj8MJkuUOgQ",
    "Перепись СССР 1959": "BQACAgIAAxkBAAIDc2msg1ui6WU68fOEHv_AFP-oA5DoAALdlAAC_jJoSVveaiHOVMDPOgQ",
    "Перепись Польши 1938": "BQACAgIAAxkBAAIDdGmsg2moAeagJnYvnb4pfQItQNevAALelAAC_jJoSbJPpGfE1E5COgQ"
}


# ===== СТАРТ =====
@bot.message_handler(commands=["start"])
def start(message):

    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add("📷 Фото", "📄 Документы")

    bot.send_message(message.chat.id, "Выбери раздел:", reply_markup=keyboard)


# ===== МЕНЮ ФОТО =====
@bot.message_handler(func=lambda m: m.text == "📷 Фото")
def photos_menu(message):

    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)

    for title in PHOTO_MAP:
        keyboard.add(title)

    keyboard.add("⬅ Назад")

    bot.send_message(message.chat.id, "Выбери фото:", reply_markup=keyboard)


# ===== МЕНЮ ДОКУМЕНТОВ =====
@bot.message_handler(func=lambda m: m.text == "📄 Документы")
def files_menu(message):

    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)

    for title in FILE_MAP:
        keyboard.add(title)

    keyboard.add("⬅ Назад")

    bot.send_message(message.chat.id, "Выбери документ:", reply_markup=keyboard)


# ===== НАЗАД =====
@bot.message_handler(func=lambda m: m.text == "⬅ Назад")
def back(message):
    start(message)


# ===== ОТПРАВКА ФОТО =====
@bot.message_handler(func=lambda m: m.text in PHOTO_MAP)
def send_photo(message):

    bot.send_photo(message.chat.id, PHOTO_MAP[message.text])


# ===== ОТПРАВКА PDF =====
@bot.message_handler(func=lambda m: m.text in FILE_MAP)
def send_file(message):

    bot.send_document(message.chat.id, FILE_MAP[message.text])


# ===== ЗАПУСК БОТА =====
def run_bot():
    while True:
        try:
            bot.infinity_polling(skip_pending=True)
        except Exception as e:
            print(e)


# ===== СТАРТ =====
if __name__ == "__main__":

    web_thread = threading.Thread(target=run_web)
    web_thread.start()

    run_bot()




# import telebot
# from telebot import types
# from flask import Flask
# import threading

# TOKEN = "8446394597:AAHxj-iGglalo2G3mOIL9JWZBFAp5QyU7-g"

# bot = telebot.TeleBot(TOKEN)
# app = Flask(__name__)


# # ===== ФЕЙКОВЫЙ СЕРВЕР ДЛЯ RENDER =====
# @app.route("/")
# def home():
#     return "Bot is running"


# def run_web():
#     app.run(host="0.0.0.0", port=10000)


# # ===== СПИСОК ФОТО =====
# PHOTO_MAP = {
#     "Письмо Рейнхарда": "AgACAgIAAxkBAAIDRmmsgLYpeRkE_-WKjrj3BzkTQ8QKAAL8E2sb_jJoSZfvaXnUO6NMAQADAgADeAADOgQ",
#     "Доклад айнзацгрупп": "AgACAgIAAxkBAAIDaGmsgm4hvmXk39a9NDkMufBUCH4hAAIPFGsb_jJoSZpKlJ--RA5kAQADAgADbQADOgQ",
#     "Доклад Гитлеру о казнях": "AgACAgIAAxkBAAIDaWmsgn9xuLWctmhXuijXX07tlGoVAAIQFGsb_jJoSUckNjR5xw8KAQADAgADeAADOgQ",
#     "Население евреев в мире": "AgACAgIAAxkBAAIDammsgo5SQf2U3k8V0pyradAF_VcZAAIRFGsb_jJoSdinz-zZEaJ7AQADAgADeAADOgQ",
#     "Отчёт Егера": "AgACAgIAAxkBAAIDaWmsgn9xuLWctmhXuijXX07tlGoVAAIQFGsb_jJoSUckNjR5xw8KAQADAgADeAADOgQ",
#     "Отчёт Корхера": "AgACAgIAAxkBAAIDRmmsgLYpeRkE_-WKjrj3BzkTQ8QKAAL8E2sb_jJoSZfvaXnUO6NMAQADAgADeAADOgQ",
#     "Отчёт Юргена Штропа": "AgACAgIAAxkBAAIDbWmsgvjrl6R9B8DlG94bQqCiPq8GAAIWFGsb_jJoSS1B9taT8AmWAQADAgADeQADOgQ",
#     "Перепись населения Львовского воеводства": "AgACAgIAAxkBAAIDbmmsgwaWc3GIIDV4tyX8-BnaKl05AAIXFGsb_jJoSYycIvqO18LQAQADAgADeQADOgQ",
#     "Распоряжение для евреев": "AgACAgIAAxkBAAIDb2msgxk2bXE_ZO7SFpu5G2DcghQvAAIYFGsb_jJoSbRY9s8JMC3sAQADAgADeAADOgQ",
#     "Религии в мире": "AgACAgIAAxkBAAIDcGmsgyhWEMyWKul3XJvGEEhHZ4OtAAIaFGsb_jJoSaSgZyFwDqbfAQADAgADeAADOgQ",
#     "Еврейское население Европы 1939-1991": "AgACAgIAAxkBAAIDcWmsgzLwVdBm4dt7TqUVC8UviuFWAAIbFGsb_jJoSTKLkf9lRFXQAQADAgADeQADOgQ",
# }


# # ===== СПИСОК PDF =====
# FILE_MAP = {
#     "Перепись СССР 1939": "BQACAgIAAxkBAAIDcmmsg0oKx3HbZITML7LQhbuKUK6KAALalAAC_jJoSdtIPj8MJkuUOgQ",
#     "Перепись СССР 1959": "BQACAgIAAxkBAAIDc2msg1ui6WU68fOEHv_AFP-oA5DoAALdlAAC_jJoSVveaiHOVMDPOgQ",
#     "Перепись Польши 1938": "BQACAgIAAxkBAAIDdGmsg2moAeagJnYvnb4pfQItQNevAALelAAC_jJoSbJPpGfE1E5COgQ"
# }


# # ===== СТАРТ =====
# @bot.message_handler(commands=["start"])
# def start(message):

#     keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
#     keyboard.add("📷 Фото", "📄 Документы")

#     bot.send_message(message.chat.id, "Выбери раздел:", reply_markup=keyboard)


# # ===== МЕНЮ ФОТО =====
# @bot.message_handler(func=lambda m: m.text == "📷 Фото")
# def photos_menu(message):

#     keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)

#     for title in PHOTO_MAP:
#         keyboard.add(title)

#     keyboard.add("⬅ Назад")

#     bot.send_message(message.chat.id, "Выбери фото:", reply_markup=keyboard)


# # ===== МЕНЮ ДОКУМЕНТОВ =====
# @bot.message_handler(func=lambda m: m.text == "📄 Документы")
# def files_menu(message):

#     keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)

#     for title in FILE_MAP:
#         keyboard.add(title)

#     keyboard.add("⬅ Назад")

#     bot.send_message(message.chat.id, "Выбери документ:", reply_markup=keyboard)


# # ===== НАЗАД =====
# @bot.message_handler(func=lambda m: m.text == "⬅ Назад")
# def back(message):
#     start(message)


# # ===== ОТПРАВКА ФОТО =====
# @bot.message_handler(func=lambda m: m.text in PHOTO_MAP)
# def send_photo(message):

#     bot.send_photo(message.chat.id, PHOTO_MAP[message.text])


# # ===== ОТПРАВКА PDF =====
# @bot.message_handler(func=lambda m: m.text in FILE_MAP)
# def send_file(message):

#     bot.send_document(message.chat.id, FILE_MAP[message.text])


# def run_bot():
#     bot.infinity_polling(skip_pending=True)


# # ===== ЗАПУСК =====
# if __name__ == "__main__":

#     t1 = threading.Thread(target=run_web)
#     t1.start()


#     run_bot()
