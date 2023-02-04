from telebot import *
from keyboa import Keyboa
import os
from gen import *

button1 = [[{'Заоблачный перчик 🌶': '1'}, {'Гриб руккхашава 🍄': '2'}], {'Гард': '3'}]
close = [{'Назад': '0'}]
kb1 = Keyboa(items=button1)
kb_close = Keyboa(items=close)
