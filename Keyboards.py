from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

buttons = [
    [KeyboardButton(text="Первый")],
    [KeyboardButton(text="Второй")],
    [KeyboardButton(text="Третий")],
]


menu_keyboard = ReplyKeyboardMarkup(
    keyboard=buttons,
    resize_keyboard=True,
    one_time_keyboard=True,
    row_width=1,
)