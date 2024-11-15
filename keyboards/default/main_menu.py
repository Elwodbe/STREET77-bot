from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


menu_kb = ReplyKeyboardMarkup(
            [
                [KeyboardButton("🍽 Menyu")],
                [KeyboardButton('📖 Buyurtmalar tarixi'), KeyboardButton("✍️ Fikr bildirish")],
                [KeyboardButton("ℹ️ Ma'lumot"), KeyboardButton("☎️ Biz bilan aloqa")],
                [KeyboardButton("⚙️Sozlamalar")]
            ],
            resize_keyboard=True
        )

zakaz_mi = ReplyKeyboardMarkup(
    [
        [KeyboardButton("🚙Yetkazib berish")],[KeyboardButton("🏃 Olib ketish")],
        [KeyboardButton("⬅️ Ortga")]
    ],
    resize_keyboard=True
)


sozlamalar_btn = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton("Ismni o'zgartirish"), KeyboardButton("📱 Raqamni o'zgartirish")],
        [KeyboardButton("🏙 Shaharni o'zgartirish"), KeyboardButton("🇺🇿 Tilni o'zgartirish")],
        [KeyboardButton("⬅️ Ortga")]
    ],
    resize_keyboard=True
)