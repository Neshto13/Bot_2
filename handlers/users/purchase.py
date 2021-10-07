import logging
import sqlite3 as sq

from aiogram.dispatcher.filters import Command
from aiogram.types import Message, CallbackQuery

from keyboards.inline.callback_datas import buy_callback
from keyboards.inline.choice_buttons import choice, keyboard_485, keyboard_492, keyboard_493
from loader import dp, bot


@dp.message_handler(Command("start"))
async def start(message: Message):
    await message.answer(text="Я бот который знает расписание маршруток. Выберите номер маршрутки",
                         reply_markup=choice)


# Попробуйем отловить по встроенному фильтру, где в нашем call.data содержится "485"
@dp.callback_query_handler(text_contains="485")
async def marsh_485(call: CallbackQuery):
    # Обязательно сразу сделать answer, чтобы убрать "часики" после нажатия на кнопку.
    # Укажем cache_time, чтобы бот не получал какое-то время апдейты, тогда нижний код не будет выполняться.
    await call.answer(cache_time=60)

    callback_data = call.data

    # Отобразим что у нас лежит в callback_data
    # logging.info(f"callback_data='{callback_data}'")
    logging.info(f"{callback_data=}")

    await call.message.answer("Вы выбрали маршрутку № 485. Выберите направление:",
                              reply_markup=keyboard_485)


@dp.callback_query_handler(text_contains="492")
async def marsh_492(call: CallbackQuery):

    await call.answer(cache_time=60)
    callback_data = call.data
    logging.info(f"{callback_data=}")

    await call.message.answer("Вы выбрали маршрутку № 492. Выберите направление:",
                              reply_markup=keyboard_492)


@dp.callback_query_handler(text_contains="493")
async def marsh_493(call: CallbackQuery):

    await call.answer(cache_time=60)
    callback_data = call.data
    logging.info(f"{callback_data=}")

    await call.message.answer("Вы выбрали маршрутку № 493. Выберите направление:",
                              reply_markup=keyboard_493)


@dp.callback_query_handler(text="cancel")
async def cancel_buying(call: CallbackQuery):

    await call.answer("Вы отменили поездку!", show_alert=True)

    # Отправляем пустую клавиатуру изменяя сообщение, для того, чтобы ее убрать из сообщения!
    await call.message.edit_reply_markup(reply_markup=None)

con = sq.connect('Raspisanie_bus_Test1BD.db3')
cur = con.cursor()

# cur.execute("SELECT number FROM roat")
# res = cur.fetchall()
#
# lst1 =[]
# for el in range(len(res)):
#      lst = list(res[el])
#      for i in lst:
#           lst1.append(i)
# # print(res)
# print((lst1),'из этого списка мы ищем 485')
# print(lst1[0], "нашли")
#
# cur.execute("SELECT stop_bus FROM stop_roat WHERE roat_number=?", ([lst1[0]]))
# res2 = cur.fetchall()
#
# lst2 =[]
# for el in range(len(res2)):
#      lst = list(res2[el])
#      for i in lst:
#           lst2.append(i)
# print(lst2)