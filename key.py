from telebot import *
from keyboa import Keyboa
import os
from gen import *

button1 = [[{'Заоблачный перчик 🌶': '1'}, {'Гриб руккхашава 🍄': '2'}], {'Гард': '3'}, {'Глазурная лилия🌺': '4'}]
button2 = [[{'Маршруты': '11'}, {'Персонажи': '12'}, {'Артифакты': '13'}], [{'Оружие': '14'}, {'Тир лист': '15'}, {'Расписание': '16'}], {'Помощь': '17'}]
close = [{'Назад': '0'}]
button3 = [{'Сяо': '20'}]
kb1 = Keyboa(items=button1)
kb2 = Keyboa(items=button2)
kb3 = Keyboa(items=button3)
kb_close = Keyboa(items=close)
