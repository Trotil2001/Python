from telegram import Update
from telegram.ext import ContextTypes, CallbackContext
import datetime
from spy import *


async def echo(update, context):
    await context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text + ' - эхо'.upper())

async def unknown(update, context):
    if update.message.text == '/sum':
        sum_command()
    else:
        await context.bot.send_message(chat_id=update.effective_chat.id, 
                                   text="Извени, Я не знаю такую комманду.")


async def hi_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(update, context)
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(update, context)
    await update.message.reply_text(f'/hi\n/time\n/Help\n/sum x y\n/dif x y\n/mult x y\n/div x y')

async def time_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(update, context)
    await update.message.reply_text(f'Time {datetime.datetime.now().time()}')

async def sum_command(update: Update, context: CallbackContext):
    log(update, context)
    context.bot.send_message(chat_id=update.effective_chat.id, text='Введи число X:')
    msg = update.message.text
    items = msg.split()
    x = float(items[1])
    y = float(items[2])
    await update.message.reply_text(f'{x} + {y} = {x+y}')

async def dif_command(update: Update, context: CallbackContext):
    log(update, context)
    msg = update.message.text
    items = msg.split()
    x = float(items[1])
    y = float(items[2])
    await update.message.reply_text(f'{x} - {y} = {x-y}')

async def mult_command(update: Update, context: CallbackContext):
    log(update, context)
    msg=update.message.text
    items = msg.split()
    x = float(items[1])
    y = float(items[2])
    await update.message.reply_text(f'{x} * {y} = {x*y}')

async def div_command(update: Update, context: CallbackContext):
    log(update, context)
    msg=update.message.text
    items = msg.split()
    x = float(items[1])
    y = float(items[2])
    await update.message.reply_text(f'{x} / {y} = {x/y}')


    







