# import os
# import django
# from django_telegram_bot.settings import DATABASES
# # from user_data.models import UserData
# from telegram import Update
# from telegram.ext import Updater, CommandHandler, CallbackContext
# from dotenv import load_dotenv


# def start(update: Update, context : CallbackContext) -> None:
#     # user_id = update.effective_user.id
#     # try:
#     #     user_data = UserData.objects.get(id = user_id)
#     #     update.message.reply_text(f"Welcome back {user_data.first_name}!")
#     # except UserData.DoesNotExist:
#     #     new_user  = UserData(
#     #         id = user_id,
#     #         first_name = update.effective_user.first_name,
#     #         last_name = update.effective_user.last_name,
#     #         username = update.effective_user.username
            
#     #     )
#     #     new_user.save()
#     #     update.message.reply_text("Welcome to django-telgram-bot!")
#     update.message.reply_text("Welcome to django-telgram-bot!")    
        
        
# def main() -> None:
#     load_dotenv()
#     token = os.getenv('TOKEN')
#     updater = Updater(token, use_context=True)
#     dispatcher = updater.dispatcher
#     dispatcher.add_handler(CommandHandler('start', start))
#     updater.start_polling()
#     updater.idle()
    
    
# if __name__ == "__main__":
#     main()
    
    
    
    
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Define a command handler function
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Hello, I am a bot!")

# Initialize the application with your bot token
application = ApplicationBuilder().token("your_bot_token").build()

# Register the /start command
start_handler = CommandHandler('start', start)
application.add_handler(start_handler)

# Run the bot until you press Ctrl-C or the process receives SIGINT, SIGTERM or SIGABRT
application.run_polling()    