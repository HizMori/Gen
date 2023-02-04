from telebot import *

keyboard = types.InlineKeyboardMarkup(row_width=2)
callback_button1 = types.InlineKeyboardButton(text='Заоблачный перчик 🌶', callback_data='1')
callback_button2 = types.InlineKeyboardButton(text='Гриб руккхашава 🍄', callback_data='2')
callback_button3 = types.InlineKeyboardButton(text='Гард', callback_data='3')
keyboard.add(callback_button1, callback_button2, callback_button3)