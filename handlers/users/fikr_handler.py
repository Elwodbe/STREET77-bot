from aiogram import types
from loader import dp
from loader import bot
from data.config import ADMINS
from keyboards.default.main_menu import menu_kb
from keyboards.default.main_menu import zakaz_mi
from keyboards.default.main_menu import sozlamalar_btn



@dp.message_handler(text = "Hammasi yoqdi ♥️")
async def send_admin(message: types.Message):
    for i in ADMINS:
        await bot.send_message(chat_id=i,text="Sizga bitta <b>Hammasi yoqdi ♥️</b> keldi.")
    await message.answer("Rahmat xabaringiz adminga yuborildi!",reply_markup=menu_kb)
    

@dp.message_handler(text="Yaxshi ⭐️⭐️⭐️⭐️")
async def send_admins(message:types.Message):
    for i in ADMINS:
        await bot.send_message(chat_id=i,text="Sizga bitta <b>Yaxshi</b> keldi.")
    await message.answer("Rahmat xabaringiz adminga yuborildi!",reply_markup=menu_kb)

@dp.message_handler(text="Yoqmadi ⭐️⭐️⭐️")
async def send_admin2(message:types.Message):
    for i in ADMINS:
        await bot.send_message(chat_id=i,text="Sizga bitta <b>Yoqmadi</b> keldi.")
    await message.answer("Rahmat xabaringiz adminga yuborildi!",reply_markup=menu_kb)

@dp.message_handler(text="Yomon ⭐️⭐️")
async def send_admin3(message:types.Message):
    for i in ADMINS:
        await bot.send_message(chat_id=i,text="Sizga bitta <b>Yomon</b> keldi.")
    await message.answer("Rahmat xabaringiz adminga yuborildi!",reply_markup=menu_kb)


@dp.message_handler(text="Juda yomon 👎🏻")
async def send_admin4(message:types.Message):
    for i in ADMINS:
        await bot.send_message(chat_id=i,text="Sizga bitta <b>Juda yomon 👎🏻</b> keldi.")
    await message.answer("Rahmat xabaringiz adminga yuborildi!",reply_markup=menu_kb)


@dp.message_handler(text="⬅️ Ortga")
async def ortga_qaytish(message:types.Message):
    await message.answer("<b>Bosh menyu</b>",reply_markup=menu_kb)

@dp.message_handler(text="🍽 Menyu")
async def menyu(message:types.Message):
    await message.answer("Buyurtmani <b>o'zingiz</b> olib keting yoki <b>Yetkazib berishni</b> tanlang",reply_markup=zakaz_mi)

@dp.message_handler(text="⚙️Sozlamalar")
async def sozlamalar_btn1(message:types.Message):
    await message.answer("<b>Harakat tanlang: </b>",reply_markup=sozlamalar_btn)

@dp.message_handler(text="Ismni o'zgartirish")
async def ism_ozgartir(message:types.Message):
    