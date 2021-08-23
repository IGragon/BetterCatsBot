from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from keyboards.inline.callback_datas import help_callback

help_markup = InlineKeyboardMarkup(inline_keyboard=[  # inline keyboard for helper
    [
        InlineKeyboardButton(text="Cat", callback_data=help_callback.new(command="cat"))
    ],
    [
        InlineKeyboardButton(text="Help", callback_data=help_callback.new(command="help"))
    ]
])
