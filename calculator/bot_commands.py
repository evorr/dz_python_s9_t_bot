from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import datetime
import spy
import model


async def start_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    spy.log(update, context)
    await update.message.reply_text(f'Это калькулятор рациональных и комплексных чисел.\n'
                                    f'Введите числа через пробел после команды.'
                                    f'/sum - сложение\n/sub - вычитание\n/mult - умножение\n/div - деление')


async def menu_operations(update: Update, context: ContextTypes.DEFAULT_TYPE):
    spy.log(update, context)
    await update.message.reply_text(f'/sum - сложение\n/sub - вычитание\n/mult - умножение\n/div - деление')


async def hi_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    spy.log(update, context)
    await update.message.reply_text(f'Hi {update.effective_user.first_name}')


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    spy.log(update, context)
    await update.message.reply_text(f'/hi\n/time\n/help\n/menu')


async def time_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    spy.log(update, context)
    await update.message.reply_text(f'{datetime.datetime.now().time()}')


async def sum_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    spy.log(update, context)
    msg = update.message.text
    x, y = model.get_numbers(msg)
    result = model.sum_num(x, y)
    await update.message.reply_text(f'{x} + {y} = {result}')


async def sub_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    spy.log(update, context)
    msg = update.message.text
    x, y = model.get_numbers(msg)
    result = model.sub_num(x, y)
    await update.message.reply_text(f'{x} - {y} = {result}')


async def mult_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    spy.log(update, context)
    msg = update.message.text
    x, y = model.get_numbers(msg)
    result = model.mult_num(x, y)
    await update.message.reply_text(f'{x} * {y} = {result}')


async def divis_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    spy.log(update, context)
    msg = update.message.text
    x, y = model.get_numbers(msg)
    result = model.div_num(x, y)
    await update.message.reply_text(f'{x} / {y} = {result}')