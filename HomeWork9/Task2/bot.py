import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters
from bot_commands import *



logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

if __name__ == '__main__':
    app = ApplicationBuilder().token("TOKEN").build()

    app.add_handler(CommandHandler('start', help_command))
    app.add_handler(CommandHandler('help', help_command))
    app.add_handler(CommandHandler("hi", hi_command))
    app.add_handler(CommandHandler("time", time_command))
    app.add_handler(CommandHandler("sum", sum_command))
    app.add_handler(CommandHandler("dif", dif_command))
    app.add_handler(CommandHandler("milt", mult_command))
    app.add_handler(CommandHandler("div", div_command))
    echo_handler = MessageHandler(filters.Text and (~filters.COMMAND), echo)
    unknown_handler = MessageHandler(filters.COMMAND, unknown)
    # app.add_handler(echo_handler)
    app.add_handler(unknown_handler)
    
    app.run_polling()