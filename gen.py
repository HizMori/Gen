from media import *
from telebot import *
from key import *

bot = telebot.TeleBot('5941098660:AAExtbCvBFnHUPBoXUBLLvU4NO4nbOK1DMo')

@bot.message_handler(commands = ['start'])
def satart_message(message):
    bot.send_video(message.chat.id, video='https://upload-os-bbs.mihoyo.com/upload/2021/02/20/11910332/b698396410c67c404e561e08d6cafe6c_7932095444786076935.gif')
    bot.send_message(message.chat.id, hello)

@bot.message_handler(commands = ['routes'])
def routes_message(message):
    bot.send_message(message.chat.id, 'Какой ресурс вы хотите собрать?', reply_markup=kb1())

@bot.callback_query_handler(func=lambda call:True)
def callback(call):
    if call.message:
        if call.data == '0':
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text='Какой ресурс вы хотите собрать?', reply_markup=kb1())
        elif call.data == '1':
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                                  text='🌶 *Заоблачный перчик* 🌶', parse_mode='Markdown')
            bot.send_media_group(call.message.chat.id, media_perets1)
            bot.send_media_group(call.message.chat.id, media_perets2)
            bot.send_message(call.message.chat.id, 'Хотите вернуться?', reply_markup=kb_close())
        elif call.data == '2':
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                                  text='🍄 *Гриб руккхашава* 🍄', parse_mode='Markdown')
            bot.send_media_group(call.message.chat.id, media_grib1)
            bot.send_message(call.message.chat.id, 'Хотите вернуться?', reply_markup=kb_close())
        elif call.data == '3':
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                                  text='*Гард*', parse_mode='Markdown')
            bot.send_media_group(call.message.chat.id, media_gard1)
            bot.send_media_group(call.message.chat.id, media_gard2)
            bot.send_message(call.message.chat.id, 'Хотите вернуться?', reply_markup=kb_close())
        elif call.data == '4':
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                                  text='🌺 *Глазурная лилия* 🌺', parse_mode='Markdown')
            bot.send_media_group(call.message.chat.id, media_gard1)
            bot.send_media_group(call.message.chat.id, media_gard2)
            bot.send_message(call.message.chat.id, 'Хотите вернуться?', reply_markup=kb_close())

print("Бот запущен!!!")

if __name__ == "__main__":
    bot.polling(none_stop=True)