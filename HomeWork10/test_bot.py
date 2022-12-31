import logging
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, Update
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
    ConversationHandler,
    MessageHandler,
    filters,
)

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)

CHOOSING, TYPING_REPLY, TYPING_CHOICE = range(3)


reply_keyboard = [["Sum", "Dif", "Mult", "Div"]]

# Dict = ()
markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)

def facts_to_str(user_data) -> str:
    """Вспомогательная функция для форматирования 
    собранной информации о пользователе."""
    facts = [f"{key} - {value}" for key, value in user_data.items()]
    return "\n".join(facts).join(["\n", "\n"])

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Начvало разговора, просьба ввести данные."""
    await update.message.reply_text(
        "Привет. Выбери прерацию.",
        reply_markup=markup,
    )
    return CHOOSING

async def regular_choice(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Запрос информации о выбранном предопределенном выборе."""
    text = update.message.text
    context.user_data["choice"] = text
    await update.message.reply_text(f"Выбрал {text.lower()}? Хорошо, давай решим это!")
    return TYPING_REPLY


async def received_information(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Store info provided by user and ask for the next category."""
    user_data = context.user_data
    text = update.message.text
    category = user_data["choice"]
    user_data[category] = text
    msg = text.split()
    x = int(msg[0])
    y = int(msg[1])
    res = 0
    op = user_data["choice"]
    if op == 'Sum':
        res = x + y
        op='+'
    if op == 'Dif':
        res = x - y
        op='-'
    if op == 'Mult':
        res = x * y
        op='*'
    if op == 'Div':
        res = x / y
        op='/'

    del user_data["choice"]

    await update.message.reply_text(
        "Результат операции:"
        f"{user_data}  {x} {op} {y} = {res}",
        reply_markup=markup,
    )
    return CHOOSING

async def done(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Вывод собранной информации и завершение разговора."""
    user_data = context.user_data
    if "choice" in user_data:
        del user_data["choice"]

    await update.message.reply_text(
        f"I learned these facts about you: {facts_to_str(user_data)}Until next time!",
        reply_markup=ReplyKeyboardRemove(),
    )
    user_data.clear()
    return ConversationHandler.END


if __name__ == "__main__":
    application = Application.builder().token("TOKEN").build()

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler("start", start)],
        states={
            CHOOSING: [
                MessageHandler(
                    # filters.Regex("^(Age|Favourite colour|Number of siblings)$"), regular_choice
                    filters.Regex("^(Sum|Dif|Mult|Div)$"), regular_choice
                ),
            ],
            TYPING_REPLY: [
                MessageHandler(
                    filters.TEXT & ~(filters.COMMAND | filters.Regex("^Done$")),
                    received_information,
                ),
            ],
        },
        fallbacks=[MessageHandler(filters.Regex("^Done$"), done)],
    )

    application.add_handler(conv_handler)
    # Запуск бота.
    application.run_polling()