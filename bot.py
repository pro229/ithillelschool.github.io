from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN = "8144752824:AAHgwuzeHwTY28ZQK7x0DUtSsnBKdqUcw4g"
PARTNER_LINK = "https://reg.eda.yandex.ru/?advertisement_campaign=forms_for_agents&user_invite_code=1510b776dba5472fb4631cb350890b56&utm_content=blank"

main_keyboard = ReplyKeyboardMarkup(
    [["📋 Условия", "❓ Вопросы"], ["🔗 Регистрация", "💬 Написать"]],
    resize_keyboard=True
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Привет! 👋 Работа курьером в Яндекс Доставке — от 3000₽ в день.\n\nВыбери, что тебя интересует:",
        reply_markup=main_keyboard
    )

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    if text == "📋 Условия":
        await update.message.reply_text(
            "📋 Условия работы:\n"
            "- Доход от 3000₽ в день\n"
            "- Без опыта\n"
            "- Пешком, на велике или авто\n"
            "- Свободный график\n"
            "- Выплаты каждый день"
        )
    elif text == "❓ Вопросы":
        await update.message.reply_text(
            "❓ Частые вопросы:\n"
            "— Нужен ли опыт? ❌ Нет\n"
            "— Где работаем? 📍 Тюмень\n"
            "— Когда платят? 💸 Каждый день\n"
            "— Можно ли без гражданства РФ? ✅ Да, с ИНН"
        )
    elif text == "🔗 Регистрация":
        await update.message.reply_text(f"👉 Перейди по ссылке и зарегистрируйся:\n{PARTNER_LINK}")
    elif text == "💬 Написать":
        await update.message.reply_text("📩 Напиши сюда, если что-то непонятно — я помогу!")
    else:
        await update.message.reply_text("Выбери кнопку ниже 👇", reply_markup=main_keyboard)

def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    print("Бот запущен...")
    app.run_polling()

if __name__ == "__main__":
    main()
