from aiogram.types import ReplyKeyboardRemove, KeyboardButton, ReplyKeyboardMarkup

cat_markup = ReplyKeyboardMarkup(keyboard=[  # cancel button
    [
        KeyboardButton(text="Отмена")
    ]
], resize_keyboard=True, one_time_keyboard=True)

remove_keyboard = ReplyKeyboardRemove()
