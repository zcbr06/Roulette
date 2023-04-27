import random
from telegram.ext import Updater, CommandHandler, MessageHandler, filters, CallbackQueryHandler
from telegram import ForceReply, InlineKeyboardButton, InlineKeyboardMarkup

from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler

# Создаем список переменных
global a 
global b 
b = ["Выстрел!", "Клик", "Клик", "Клик", "Клик", "Клик"] 
a = ["Выстрел!", "Клик", "Клик", "Клик", "Клик", "Клик"] 

# Функция для обработки команды /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /start is issued."""
    user = update.effective_user
    await update.message.reply_html(
        rf"Привет! {user.mention_html()}, используй (/variable)",
    )
    
# Функция для обработки команды /variable
async def get_variable(update, context):
    global a 
    if a == []: a = ["Выстрел!", "Клик", "Клик", "Клик", "Клик", "Клик"]
    var = random.choice(a)  # выбираем случайную переменную из списка  
    a.remove(var)  # удаляем выбранную переменную из списка
    await context.bot.send_message(chat_id=update.effective_chat.id, text=var)  # отправляем сообщение с выбранной переменной

# Создаем экземпляр Updater и получаем токен бота
updater = ApplicationBuilder().token('TOKEN').build()

# Создаем обработчики команд и сообщений
start_handler = CommandHandler('start', start)
get_variable_handler = CommandHandler('variable', get_variable)

# Регистрируем обработчики в диспетчере
updater.add_handler(start_handler)
updater.add_handler(get_variable_handler)

# Запускаем бота
updater.run_polling()
updater.idle()