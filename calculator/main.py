from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import bot_commands
import os
from dotenv import load_dotenv

load_dotenv()
token = os.getenv('token_tg')
app = ApplicationBuilder().token(token).build()


app.add_handler(CommandHandler("start", bot_commands.start_message))
app.add_handler(CommandHandler("menu", bot_commands.menu_operations))
app.add_handler(CommandHandler("hi", bot_commands.hi_command))
app.add_handler(CommandHandler("time", bot_commands.time_command))
app.add_handler(CommandHandler("help", bot_commands.help_command))
app.add_handler(CommandHandler("sum", bot_commands.sum_command))
app.add_handler(CommandHandler("sub", bot_commands.sub_command))
app.add_handler(CommandHandler("mult", bot_commands.mult_command))
app.add_handler(CommandHandler("div", bot_commands.divis_command))

print('server start')
app.run_polling()