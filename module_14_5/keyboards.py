from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


#kl - обычная клавиатура
kl = ReplyKeyboardMarkup(resize_keyboard=True)
button_kl_1 = KeyboardButton(text='Расчитать')
button_kl_2 = KeyboardButton(text='Информация')
button_kl_3 = KeyboardButton(text='Арендовать')
button_kl_4 = KeyboardButton(text='Регистрация')
kl.add(button_kl_1, button_kl_2, button_kl_3, button_kl_4)

#kb - инлайн клавиатура Расчет и Формула
kb = InlineKeyboardMarkup(resize_keyboard=True)
button_kb_1 = InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='calories')
button_kb_2 = InlineKeyboardButton(text='Формулы расчёта', callback_data='formulas')
kb.add(button_kb_1, button_kb_2)

#menu_kb - Меню Продуктов
menu_kb = InlineKeyboardMarkup(resize_keyboard=True)
button_mn_1 = InlineKeyboardButton(text='Мотоцикл1', callback_data='product_buying')
button_mn_2 = InlineKeyboardButton(text='Мотоцикл2', callback_data='product_buying')
button_mn_3 = InlineKeyboardButton(text='Мотоцикл3', callback_data='product_buying')
button_mn_4 = InlineKeyboardButton(text='Мотоцикл4', callback_data='product_buying')
menu_kb.add(button_mn_1, button_mn_2, button_mn_3, button_mn_4)