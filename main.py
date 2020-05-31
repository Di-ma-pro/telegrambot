import telebot
import config
from telebot import types
import random

bot = telebot.TeleBot(config.TOKEN)
markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

b1 = types.KeyboardButton("Рандомное число")
b2 = types.KeyboardButton("Inline клавиатура")

markup.add(b1, b2)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Привет, {0.first_name}!".format(message.from_user, bot.get_me()), parse_mode='html', reply_markup=markup)

@bot.message_handler(content_types=['text'])
def b(message):
    if message.text == "Рандомное число":
        bot.send_message(message.chat.id, str(random.randint(-100,100)))
    elif message.text == "Inline клавиатура":
        inline = types.InlineKeyboardMarkup(row_width=2)
        i1 = types.InlineKeyboardButton("Ok", callback_data='ok')
        i2 = types.InlineKeyboardButton("Cancel", callback_data='cancel')
        inline.add(i1, i2)
        bot.send_message(message.chat.id, "Inline", reply_markup=inline)
    else:
        bot.send_message(message.chat.id, "Я вас не понимаю")
# @bot.callback_query_handler(func=lambda call: True)
# def callback_inline(call):
#     try:
#         if call.message:
#             if call.data == 'ok':
#                 bot.send_message(message.chat.id, "Ok")
#             elif call.data == 'cancel':
#                 bot.send_message(message.chat.id, "Cancel")
#                 bot.edit_message_text(message.chat.id, call.message.message_id, "Inline", reply_markup=None)
#                 bot.answer_callback_query(call.message.chat.id, True, "Canceled")
#     except Exception as e:
#         print(repr(e))
bot.polling(none_stop=True)
