import telebot
from telebot import types, callback_data
bot = telebot.TeleBot('5941098660:AAExtbCvBFnHUPBoXUBLLvU4NO4nbOK1DMo')

@bot.message_handler(commands = ['start'])
def satart_message(message):
    bot.send_photo(message.chat.id, photo='https://rare-gallery.com/thumbnail/54299-Xiao-Genshin-Impact-Black-Hair-Green-Hair-Yellow.jpg')
    keyboard = types.InlineKeyboardMarkup()
    callback_button = types.InlineKeyboardButton(text="Нажми меня", callback_data="1")
    keyboard.add(callback_button)
    bot.send_message(message.chat.id, f"Доброго денёчка {message.from_user.first_name}!", reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call:True)
def callback(call):
    if call.message:
        if call.data == '1':
            bot.send_video(call.message.chat.id, video='https://upload-os-bbs.mihoyo.com/upload/2021/02/20/11910332/b698396410c67c404e561e08d6cafe6c_7932095444786076935.gif')
            bot.send_message(call.message.chat.id, "Крассивый Сяо)")

print("Бот запущен!!!")

if __name__ == "__main__":
    bot.polling(none_stop=True)