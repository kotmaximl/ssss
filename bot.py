import telebot
from telebot import types

TOKEN = "8446394597:AAHxj-iGglalo2G3mOIL9JWZBFAp5QyU7-g"

bot = telebot.TeleBot(TOKEN)


# ===== СПИСОК ФОТО (теперь тут file_id) =====
PHOTO_MAP = {
    "Письмо Рейнхарда": "ID_ФОТО_1",
    "Доклад айнзацгрупп": "ID_ФОТО_2",
    "Доклад Гитлеру о казнях": "ID_ФОТО_3",
    "Население евреев в мире": "ID_ФОТО_4",
    "Отчёт Егера": "ID_ФОТО_5",
    "Отчёт Корхера": "ID_ФОТО_6",
    "Отчёт Юргена Штропа": "ID_ФОТО_7",
    "Перепись населения Львовского воеводства": "ID_ФОТО_8",
    "Распоряжение для евреев": "ID_ФОТО_9",
    "Религии в мире": "ID_ФОТО_10",
    "Еврейское население Европы 1939-1991": "ID_ФОТО_11",
}


# ===== СПИСОК PDF (теперь тут file_id) =====
FILE_MAP = {
    "Перепись СССР 1939": "ID_PDF_1",
    "Перепись СССР 1959": "ID_PDF_2",
    "Перепись Польши 1938": "ID_PDF_3"
}


# ===== СТАРТ =====
@bot.message_handler(commands=["start"])
def start(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add("📷 Фото", "📄 Документы")

    bot.send_message(
        message.chat.id,
        "Выбери раздел:",
        reply_markup=keyboard
    )


# ===== МЕНЮ ФОТО =====
@bot.message_handler(func=lambda m: m.text == "📷 Фото")
def photos_menu(message):

    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)

    for title in PHOTO_MAP.keys():
        keyboard.add(title)

    keyboard.add("⬅ Назад")

    bot.send_message(
        message.chat.id,
        "Выбери фото:",
        reply_markup=keyboard
    )


# ===== МЕНЮ ДОКУМЕНТОВ =====
@bot.message_handler(func=lambda m: m.text == "📄 Документы")
def files_menu(message):

    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)

    for title in FILE_MAP.keys():
        keyboard.add(title)

    keyboard.add("⬅ Назад")

    bot.send_message(
        message.chat.id,
        "Выбери документ:",
        reply_markup=keyboard
    )


# ===== НАЗАД =====
@bot.message_handler(func=lambda m: m.text == "⬅ Назад")
def back(message):
    start(message)


# ===== ОТПРАВКА ФОТО =====
@bot.message_handler(func=lambda m: m.text in PHOTO_MAP)
def send_photo(message):

    file_id = PHOTO_MAP.get(message.text)

    try:
        bot.send_photo(message.chat.id, file_id)
    except Exception as e:
        bot.send_message(message.chat.id, "⚠️ Фото не найдено")
        print(e)


# ===== ОТПРАВКА PDF =====
@bot.message_handler(func=lambda m: m.text in FILE_MAP)
def send_file(message):

    file_id = FILE_MAP.get(message.text)

    try:
        bot.send_document(message.chat.id, file_id)
    except Exception as e:
        bot.send_message(message.chat.id, "⚠️ Документ не найден")
        print(e)


# ===== ПОЛУЧЕНИЕ file_id (временно) =====
@bot.message_handler(content_types=["photo", "document"])
def get_file_id(message):

    if message.photo:
        print("PHOTO ID:", message.photo[-1].file_id)

    if message.document:
        print("DOCUMENT ID:", message.document.file_id)


# ===== ЗАПУСК =====
bot.infinity_polling(skip_pending=True)
