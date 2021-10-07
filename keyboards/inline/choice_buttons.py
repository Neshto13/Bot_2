import sqlite3 as sq

from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, inline_keyboard
from config import URL_MARSH_485, URL_MARSH_492, URL_MARSH_493
from keyboards.inline.callback_datas import buy_callback

# с помощью row_width и insert.
choice = InlineKeyboardMarkup(row_width=3)

marsh_485 = InlineKeyboardButton(text="485", callback_data=buy_callback.new(item_name="485", quantity=1))
choice.insert(marsh_485)
marsh_492 = InlineKeyboardButton(text="492", callback_data=buy_callback.new(item_name="492", quantity=1))
choice.insert(marsh_492)
marsh_493 = InlineKeyboardButton(text="493", callback_data=buy_callback.new(item_name="493", quantity=1))
choice.insert(marsh_493)

cancel_button = InlineKeyboardButton(text="Отмена", callback_data="cancel")
choice.insert(cancel_button)

choice_2 = InlineKeyboardMarkup(row_width=2)
# Клавиатуры со ссылками на сайт
keyboard_485 = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Комаровский рынок", url=URL_MARSH_485),
        InlineKeyboardButton(text="Петруся Бровки", url=URL_MARSH_485),
    ]
])

keyboard_492 = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="ДС Дружная", url=URL_MARSH_492),
        InlineKeyboardButton(text="Мачулищи", url=URL_MARSH_492)
    ]
])

keyboard_493 = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="ДС Дружная-1", url=URL_MARSH_493),
        InlineKeyboardButton(text="Самохваловичи", url=URL_MARSH_493)

    ]
])