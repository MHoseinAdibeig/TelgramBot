# from rest_framework import status
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework.authentication import TokenAuthentication
# from rest_framework.permissions import IsAuthenticated
# from rest_framework.parsers import MultiPartParser, FormParser
import os
from django_telegram_bot.celery import app
from asgiref.sync import sync_to_async
from django.conf import settings
from celery import shared_task
# from .models import Gadget, State, Analysis, SampleDetail, Result
from .models import Tweet
# from .analyser.MotilityGadget.semenAnalysis import semenAnalysis
# @shared_task()
@app.task(name="telegram_bot")
def sample_task():
        try:
            from aiogram import Bot, Dispatcher, types
            from aiogram import executor
            from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

            TOKEN = '7209577533:AAEnZ1mwZLI-AGx0TBAGmbDaES-VhOyQkc8'
            bot = Bot(token=TOKEN)
            dp = Dispatcher(bot)

            # Custom command: /uppercase
            @dp.message_handler(commands=['uppercase'])
            async def uppercase_command(message: types.Message):
                # Get the user's message
                tweet = await sync_to_async(Tweet.objects.first)()
                user_text = message.text[len('/uppercase '):]  # Remove the command part
                # Convert to uppercase
                uppercase_text = user_text.upper()
                # Reply with the uppercase text
                await message.reply(f"Uppercase: {tweet.question}\nChat ID: {message.chat.id}\nUsername: {message.chat.username}")

            # Inline keyboard setup (similar to your existing code)
            button1 = InlineKeyboardButton(text="button1", callback_data="In_First_button")
            button2 = InlineKeyboardButton(text="button2", callback_data="In_Second_button")
            keyboard_inline = InlineKeyboardMarkup().add(button1, button2)

            @dp.message_handler(commands=['start'])
            async def check(message: types.Message):
                await message.reply("Hi! How are you?", reply_markup=keyboard_inline)

            @dp.callback_query_handler(text=["In_First_button", "In_Second_button"])
            async def check_button(call: types.CallbackQuery):
                if call.data == "In_First_button":
                    await call.message.answer("Hi! This is the first inline keyboard button.")
                if call.data == "In_Second_button":
                    await call.message.answer("Hi! This is the second inline keyboard button.")
                await call.answer()

            executor.start_polling(dp)
            # analysis.state = State.objects.get(code="waiting_for_results")
            # analysis.save()
        except Exception as e:
            raise Exception("err_analysis_badstate")

