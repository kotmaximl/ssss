# import telebot
# from telebot import types
# import os
# import time

# TOKEN = "8446394597:AAHxj-iGglalo2G3mOIL9JWZBFAp5QyU7-g"

# bot = telebot.TeleBot(TOKEN)

# # === ПУТИ К ПАПКАМ ===
# PHOTOS_PATH = r"C:\Users\Maxim\OneDrive\Desktop\100101\ыыыы\photos"
# FILES_PATH  = r"C:\Users\Maxim\OneDrive\Desktop\100101\ыыыы\files"


# @bot.message_handler(commands=['start'])
# def start(message):
#     keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
#     keyboard.add("📷 Фото", "📄 Документы")
#     bot.send_message(message.chat.id, "Выбери раздел:", reply_markup=keyboard)


# @bot.message_handler(func=lambda m: m.text == "📷 Фото")
# def photos_menu(message):
#     keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)

#     # 🔽 ТУТ УКАЗЫВАЕШЬ НАЗВАНИЯ ФОТО
#     keyboard.add(
#         "Фото 1",
#         "Фото 2",
#         "Фото 3",
#         "Фото 4",
#         "Фото 5",
#         "Фото 6",
#         "Фото 7",
#         "Фото 8",
#         "Фото 9",
#         "Фото 10"
        
#         # добавь остальные
#     )
#     keyboard.add("⬅ Назад")
#     bot.send_message(message.chat.id, "Выбери фото:", reply_markup=keyboard)


# @bot.message_handler(func=lambda m: m.text == "📄 Документы")
# def files_menu(message):
#     keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)

#     # 🔽 ТУТ УКАЗЫВАЕШЬ НАЗВАНИЯ PDF
#     keyboard.add(
#         "Перепись СССР 1939",
#         "Перепись СССР 1959",
#         "Перепись Польши 1938"
#     )
#     keyboard.add("⬅ Назад")
#     bot.send_message(message.chat.id, "Выбери документ:", reply_markup=keyboard)


# @bot.message_handler(func=lambda m: m.text == "⬅ Назад")
# def back(message):
#     start(message)


# @bot.message_handler(func=lambda m: m.text.startswith("Фото"))
# def send_photo(message):
#     photo_map = {
#         "Фото 1": "1.jpg",   # ← ИМЯ ФАЙЛА В ПАПКЕ photos
#         "Фото 2": "2.jpg",
#         "Фото 3": "3.jpg",
#         "Фото 4": "4.jpg",
#         "Фото 5": "5.jpg",
#         "Фото 6": "6.jpg",
#         "Фото 7": "7.jpg",
#         "Фото 8": "8.jpg",
#         "Фото 9": "9.jpg",
#         "Фото 10": "10.jpg"
        
        
#     }

#     file_name = photo_map.get(message.text)
#     if not file_name:
#         return

#     path = os.path.join(PHOTOS_PATH, file_name)
#     with open(path, "rb") as photo:
#         bot.send_photo(message.chat.id, photo)


# @bot.message_handler(func=lambda m: m.text.startswith("Документ"))
# def send_file(message):
#     file_map = {
#         "1": "1.pdf",   # ← ИМЯ ФАЙЛА В ПАПКЕ files
#         "2": "2.pdf",
#         "3": "3.pdf"
#     }

#     file_name = file_map.get(message.text)
#     if not file_name:
#         return

#     path = os.path.join(FILES_PATH, file_name)
#     with open(path, "rb") as file:
#         time.sleep(0.5)  # Небольшая задержка для лучшей работы бота
#         bot.send_document(message.chat.id, file)


# bot.infinity_polling()






# # import telebot
# # from telebot import types
# # import os
# # import time

# # TOKEN = "8446394597:AAHxj-iGglalo2G3mOIL9JWZBFAp5QyU7-g"

# # bot = telebot.TeleBot(TOKEN)

# # # === ПУТИ К ПАПКАМ ===
# # PHOTOS_PATH = r"C:\Users\Maxim\OneDrive\Desktop\100101\ыыыы\photos"
# # FILES_PATH  = r"C:\Users\Maxim\OneDrive\Desktop\100101\ыыыы\files"


# # # ===== СТАРТ =====
# # @bot.message_handler(commands=["start"])
# # def start(message):
# #     keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
# #     keyboard.add("📷 Фото", "📄 Документы")
# #     bot.send_message(
# #         message.chat.id,
# #         "Выбери раздел:",
# #         reply_markup=keyboard
# #     )


# # # ===== МЕНЮ ФОТО =====
# # @bot.message_handler(func=lambda m: m.text == "📷 Фото")
# # def photos_menu(message):
# #     keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
# #     keyboard.add(
# #         "Фото 1",
# #         "Фото 2",
# #         "Фото 3",
# #         "Фото 4",
# #         "Фото 5",
# #         "Фото 6",
# #         "Фото 7",
# #         "Фото 8",
# #         "Фото 9",
# #         "Фото 10"
# #     )
# #     keyboard.add("⬅ Назад")
# #     bot.send_message(message.chat.id, "Выбери фото:", reply_markup=keyboard)


# # # ===== МЕНЮ ДОКУМЕНТОВ =====
# # @bot.message_handler(func=lambda m: m.text == "📄 Документы")
# # def files_menu(message):
# #     keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
# #     keyboard.add(
# #         "Перепись СССР 1939",
# #         "Перепись СССР 1959",
# #         "Перепись Польши 1938"
# #     )
# #     keyboard.add("⬅ Назад")
# #     bot.send_message(message.chat.id, "Выбери документ:", reply_markup=keyboard)


# # # ===== НАЗАД =====
# # @bot.message_handler(func=lambda m: m.text == "⬅ Назад")
# # def back(message):
# #     start(message)


# # # ===== ОТПРАВКА ФОТО =====
# # @bot.message_handler(func=lambda m: m.text.startswith("Фото"))
# # def send_photo(message):
# #     photo_map = {
# #         "Письмо Рейнхарда": "1.jpg",     # ← ИМЯ ФАЙЛА В ПАПКЕ photos
# #         "Доклад айнзацгрупп": "2.jpg",
# #         "Доклад Гитлеру о казнях": "3.jpg",
# #         "Население евреев в мире": "4.jpg",
# #         "Отчёт Егера": "5.jpg",
# #         "Отчёт Корхера": "6.jpg",
# #         "Отчёт Юргена Штропа": "7.jpg",
# #         "Перепись населения Львовского воеводства": "8.jpg",
# #         "Распоряжение для евреев": "9.jpg",
# #         "Религии в мире": "10.jpg"
# #     }

# #     file_name = photo_map.get(message.text)
# #     if not file_name:
# #         return

# #     path = os.path.join(PHOTOS_PATH, file_name)

# #     try:
# #         with open(path, "rb") as photo:
# #             bot.send_photo(message.chat.id, photo)
# #     except Exception as e:
# #         bot.send_message(message.chat.id, "⚠️ Фото не найдено")
# #         print(e)


# # # ===== ОТПРАВКА PDF =====
# # @bot.message_handler(func=lambda m: m.text in [
# #     "Перепись СССР 1939",
# #     "Перепись СССР 1959",
# #     "Перепись Польши 1938"
# # ])
# # def send_file(message):
# #     file_map = {
# #         "Перепись СССР 1939": "2.pdf",   # ✔ теперь правильно
# #         "Перепись СССР 1959": "1.pdf",   # ✔ теперь правильно
# #         "Перепись Польши 1938": "3.pdf"  # ✔ без изменений
# #     }

# #     file_name = file_map.get(message.text)
# #     if not file_name:
# #         return

# #     path = os.path.join(FILES_PATH, file_name)

# #     try:
# #         with open(path, "rb") as file:
# #             time.sleep(0.5)
# #             bot.send_document(
# #                 message.chat.id,
# #                 file,
# #                 timeout=90
# #             )
# #     except Exception as e:
# #         bot.send_message(message.chat.id, "⚠️ Документ не найден")
# #         print(e)



# # # ===== ЗАПУСК =====
# # bot.infinity_polling()



# import telebot
# from telebot import types
# import os
# import time

# TOKEN = "8446394597:AAHxj-iGglalo2G3mOIL9JWZBFAp5QyU7-g"

# bot = telebot.TeleBot(TOKEN)

# # === ПУТИ К ПАПКАМ ===
# PHOTOS_PATH = r"C:\Users\Maxim\OneDrive\Desktop\100101\ыыыы\photos"
# FILES_PATH  = r"C:\Users\Maxim\OneDrive\Desktop\100101\ыыыы\files"


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
#     keyboard.add(
#         "Письмо Рейнхарда",
#         "Фото 2",
#         "Фото 3",
#         "Фото 4",
#         "Фото 5",
#         "Фото 6",
#         "Фото 7",
#         "Фото 8",
#         "Фото 9",
#         "Фото 10"
#     )
#     keyboard.add("⬅ Назад")
#     bot.send_message(message.chat.id, "Выбери фото:", reply_markup=keyboard)


# # ===== МЕНЮ ДОКУМЕНТОВ =====
# @bot.message_handler(func=lambda m: m.text == "📄 Документы")
# def files_menu(message):
#     keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
#     keyboard.add(
#         "Перепись СССР 1939",
#         "Перепись СССР 1959",
#         "Перепись Польши 1938"
#     )
#     keyboard.add("⬅ Назад")
#     bot.send_message(message.chat.id, "Выбери документ:", reply_markup=keyboard)


# # ===== НАЗАД =====
# @bot.message_handler(func=lambda m: m.text == "⬅ Назад")
# def back(message):
#     start(message)


# # ===== ОТПРАВКА ФОТО =====
# @bot.message_handler(func=lambda m: m.text.startswith("Фото"))
# def send_photo(message):
#     photo_map = {
#         "Письмо Рейнхарда": "1.jpg",     # ← ИМЯ ФАЙЛА В ПАПКЕ photos
#         "Фото 2": "2.jpg",
#         "Фото 3": "3.jpg",
#         "Фото 4": "4.jpg",
#         "Фото 5": "5.jpg",
#         "Фото 6": "6.jpg",
#         "Фото 7": "7.jpg",
#         "Фото 8": "8.jpg",
#         "Фото 9": "9.jpg",
#         "Фото 10": "10.jpg"
#     }

#     file_name = photo_map.get(message.text)
#     if not file_name:
#         return

#     path = os.path.join(PHOTOS_PATH, file_name)

#     try:
#         with open(path, "rb") as photo:
#             bot.send_photo(message.chat.id, photo)
#     except Exception as e:
#         bot.send_message(message.chat.id, "⚠️ Фото не найдено")
#         print(e)


# # ===== ОТПРАВКА PDF =====
# @bot.message_handler(func=lambda m: m.text in [
#     "Перепись СССР 1939",
#     "Перепись СССР 1959",
#     "Перепись Польши 1938"
# ])
# def send_file(message):
#     file_map = {
#         "Перепись СССР 1939": "1.pdf",   # ← ИМЯ ФАЙЛА В ПАПКЕ files
#         "Перепись СССР 1959": "2.pdf",
#         "Перепись Польши 1938": "3.pdf"
#     }

#     file_name = file_map.get(message.text)
#     if not file_name:
#         return

#     path = os.path.join(FILES_PATH, file_name)

#     try:
#         with open(path, "rb") as file:
#             time.sleep(0.5)
#             bot.send_document(
#                 message.chat.id,
#                 file,
#                 timeout=90
#             )
#     except Exception as e:
#         bot.send_message(message.chat.id, "⚠️ Документ не найден")
#         print(e)


# # ===== ЗАПУСК =====
# bot.infinity_polling()



import telebot
from telebot import types
import os
import time

TOKEN = "8446394597:AAHxj-iGglalo2G3mOIL9JWZBFAp5QyU7-g"

bot = telebot.TeleBot(TOKEN)

# === ПУТИ К ПАПКАМ ===
PHOTOS_PATH = r"C:\Users\Maxim\OneDrive\Desktop\100101\ыыыы\photos"
FILES_PATH  = r"C:\Users\Maxim\OneDrive\Desktop\100101\ыыыы\files"


# ===== СПИСОК ФОТО (ПОРЯДОК СОХРАНЯЕТСЯ) =====
PHOTO_MAP = {
    "Письмо Рейнхарда": "1.jpg",
    "Доклад айнзацгрупп": "2.jpg",
    "Доклад Гитлеру о казнях": "3.jpg",
    "Население евреев в мире": "4.jpg",
    "Отчёт Егера": "5.jpg",
    "Отчёт Корхера": "6.jpg",
    "Отчёт Юргена Штропа": "7.jpg",
    "Перепись населения Львовского воеводства": "8.jpg",
    "Распоряжение для евреев": "9.jpg",
    "Религии в мире": "10.jpg",
    "Еврейское население Европы 1939-1991": "11.jpg",
}


# ===== СПИСОК PDF =====
FILE_MAP = {
    "Перепись СССР 1939": "1.pdf",
    "Перепись СССР 1959": "2.pdf",
    "Перепись Польши 1938": "3.pdf"
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

    for title in PHOTO_MAP.keys():
        keyboard.add(title)

    keyboard.add("⬅ Назад")

    bot.send_message(message.chat.id, "Выбери фото:", reply_markup=keyboard)


# ===== МЕНЮ ДОКУМЕНТОВ =====
@bot.message_handler(func=lambda m: m.text == "📄 Документы")
def files_menu(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)

    for title in FILE_MAP.keys():
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
    file_name = PHOTO_MAP.get(message.text)
    path = os.path.join(PHOTOS_PATH, file_name)

    try:
        with open(path, "rb") as photo:
            bot.send_photo(message.chat.id, photo)
    except Exception as e:
        bot.send_message(message.chat.id, "⚠️ Фото не найдено")
        print(e)


# ===== ОТПРАВКА PDF =====
@bot.message_handler(func=lambda m: m.text in FILE_MAP)
def send_file(message):
    file_name = FILE_MAP.get(message.text)
    path = os.path.join(FILES_PATH, file_name)

    try:
        with open(path, "rb") as file:
            time.sleep(0.5)
            bot.send_document(message.chat.id, file, timeout=90)
    except Exception as e:
        bot.send_message(message.chat.id, "⚠️ Документ не найден")
        print(e)


# ===== ЗАПУСК =====
bot.infinity_polling()