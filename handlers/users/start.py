from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.default.main_menu import menu_kb
from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"<b>Bosh Menyu</b>",reply_markup=menu_kb)
