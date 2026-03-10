# import telebot
# from telebot import types
# import os
# import time

# TOKEN = "8446394597:AAHxj-iGglalo2G3mOIL9JWZBFAp5QyU7-g"

# bot = telebot.TeleBot(TOKEN)

# # === ПУТИ К ПАПКАМ ===
# PHOTOS_PATH = r"C:\Users\Maxim\OneDrive\Desktop\100101\ыыыы\photos"
# FILES_PATH  = r"C:\Users\Maxim\OneDrive\Desktop\100101\ыыыы\files"


# # ===== СПИСОК ФОТО (ПОРЯДОК СОХРАНЯЕТСЯ) =====
# PHOTO_MAP = {
#     "Письмо Рейнхарда": "1.jpg",
#     "Доклад айнзацгрупп": "2.jpg",
#     "Доклад Гитлеру о казнях": "3.jpg",
#     "Население евреев в мире": "4.jpg",
#     "Отчёт Егера": "5.jpg",
#     "Отчёт Корхера": "6.jpg",
#     "Отчёт Юргена Штропа": "7.jpg",
#     "Перепись населения Львовского воеводства": "8.jpg",
#     "Распоряжение для евреев": "9.jpg",
#     "Религии в мире": "10.jpg",
#     "Еврейское население Европы 1939-1991": "11.jpg",
# }


# # ===== СПИСОК PDF =====
# FILE_MAP = {
#     "Перепись СССР 1939": "1.pdf",
#     "Перепись СССР 1959": "2.pdf",
#     "Перепись Польши 1938": "3.pdf"
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

#     for title in PHOTO_MAP.keys():
#         keyboard.add(title)

#     keyboard.add("⬅ Назад")

#     bot.send_message(message.chat.id, "Выбери фото:", reply_markup=keyboard)


# # ===== МЕНЮ ДОКУМЕНТОВ =====
# @bot.message_handler(func=lambda m: m.text == "📄 Документы")
# def files_menu(message):
#     keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)

#     for title in FILE_MAP.keys():
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
#     file_name = PHOTO_MAP.get(message.text)
#     path = os.path.join(PHOTOS_PATH, file_name)

#     try:
#         with open(path, "rb") as photo:
#             bot.send_photo(message.chat.id, photo)
#     except Exception as e:
#         bot.send_message(message.chat.id, "⚠️ Фото не найдено")
#         print(e)


# # ===== ОТПРАВКА PDF =====
# @bot.message_handler(func=lambda m: m.text in FILE_MAP)
# def send_file(message):
#     file_name = FILE_MAP.get(message.text)
#     path = os.path.join(FILES_PATH, file_name)

#     try:
#         with open(path, "rb") as file:
#             time.sleep(0.5)
#             bot.send_document(message.chat.id, file, timeout=90)
#     except Exception as e:
#         bot.send_message(message.chat.id, "⚠️ Документ не найден")
#         print(e)


# # ===== ЗАПУСК =====
# bot.infinity_polling(skip_pending=True)





# import telebot
# from telebot import types

# TOKEN = "8446394597:AAHxj-iGglalo2G3mOIL9JWZBFAp5QyU7-g"

# bot = telebot.TeleBot(TOKEN)


# ===== СПИСОК ФОТО (теперь тут file_id) =====
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


# # ===== СПИСОК PDF (теперь тут file_id) =====
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

#     bot.send_message(
#         message.chat.id,
#         "Выбери раздел:",
#         reply_markup=keyboard
#     )


# # ===== МЕНЮ ФОТО =====
# @bot.message_handler(func=lambda m: m.text == "📷 Фото")
# def photos_menu(message):

#     keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)

#     for title in PHOTO_MAP.keys():
#         keyboard.add(title)

#     keyboard.add("⬅ Назад")

#     bot.send_message(
#         message.chat.id,
#         "Выбери фото:",
#         reply_markup=keyboard
#     )


# # ===== МЕНЮ ДОКУМЕНТОВ =====
# @bot.message_handler(func=lambda m: m.text == "📄 Документы")
# def files_menu(message):

#     keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)

#     for title in FILE_MAP.keys():
#         keyboard.add(title)

#     keyboard.add("⬅ Назад")

#     bot.send_message(
#         message.chat.id,
#         "Выбери документ:",
#         reply_markup=keyboard
#     )


# # ===== НАЗАД =====
# @bot.message_handler(func=lambda m: m.text == "⬅ Назад")
# def back(message):
#     start(message)


# # ===== ОТПРАВКА ФОТО =====
# @bot.message_handler(func=lambda m: m.text in PHOTO_MAP)
# def send_photo(message):

#     file_id = PHOTO_MAP.get(message.text)

#     try:
#         bot.send_photo(message.chat.id, file_id)
#     except Exception as e:
#         bot.send_message(message.chat.id, "⚠️ Фото не найдено")
#         print(e)


# # ===== ОТПРАВКА PDF =====
# @bot.message_handler(func=lambda m: m.text in FILE_MAP)
# def send_file(message):

#     file_id = FILE_MAP.get(message.text)

#     try:
#         bot.send_document(message.chat.id, file_id)
#     except Exception as e:
#         bot.send_message(message.chat.id, "⚠️ Документ не найден")
#         print(e)


# # ===== ПОЛУЧЕНИЕ file_id (временно) =====
# @bot.message_handler(content_types=["photo", "document"])
# def get_file_id(message):

#     if message.photo:
#         print("PHOTO ID:", message.photo[-1].file_id)

#     if message.document:
#         print("DOCUMENT ID:", message.document.file_id)


# # ===== ЗАПУСК =====
# bot.infinity_polling(skip_pending=True)


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




import telebot
from telebot import types
from flask import Flask
import threading

TOKEN = "8446394597:AAHxj-iGglalo2G3mOIL9JWZBFAp5QyU7-g"

bot = telebot.TeleBot(TOKEN)
app = Flask(__name__)


# ===== ФЕЙКОВЫЙ СЕРВЕР ДЛЯ RENDER =====
@app.route("/")
def home():
    return "Bot is running"


def run_web():
    app.run(host="0.0.0.0", port=10000)


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


def run_bot():
    bot.infinity_polling(skip_pending=True)


# ===== ЗАПУСК =====
if __name__ == "__main__":

    t1 = threading.Thread(target=run_web)
    t1.start()

    run_bot()