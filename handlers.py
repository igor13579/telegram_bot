from aiogram import types
from aiogram.filters.command import Command


from loader import dp
from Keyboards import menu_keyboard

@dp.message(Command("menu"))
async def call_menu_keyboard(message: types.Message):
    await  message.answer(
        text="Список доступных команд",
        reply_markup=menu_keyboard
    )


@dp.message(Command("dice"))
async def cmd_dice(message: types.Message):
    await message.answer_dice(emoji="🎲")


@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Привет!")


@dp.message()
async def echo(message: types.Message):
    await message.reply(message.text)



