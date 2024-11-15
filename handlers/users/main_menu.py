from aiogram import types
from keyboards.default.fikr import fikr_bt
from loader import dp

@dp.message_handler(text = "☎️ Biz bilan aloqa")
async def contact(message: types.Message):
    text = """Agar sizda Savollar/Shikoyatlar/Takliflar bo'lsa bizga 
yozishingiz mumkin: @Street77tech_bot

☎️ Telefon raqam: 71-200-73-73 / 71 200-86-86"""
    await message.answer(text)


@dp.message_handler(text = "✍️ Fikr bildirish")
async def fikr(message: types.Message):
    text = """<b>✅ Street 77ni tanlaganingiz uchun rahmat.
Agar Siz bizning hizmatlarimiz sifatini yaxshilashga 
yordam bersangiz, bundan benihoya xursand bo'lamiz.
Buning uchun 5 ballik tizim asosida baholang</b>"""
    await message.answer(text,reply_markup=fikr_bt)
