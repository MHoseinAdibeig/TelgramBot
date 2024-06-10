from django.shortcuts import render

# Create your views here.


import json
import requests
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
# from django_telegram_bot.settings import TELEGRAM_API_URL
from myapp.credentials import TELEGRAM_API_URL, URL, TOKEN
from myapp.models import User
import threading
import asyncio
from queue import Queue
# from django.utils.functional import async_to_sync

from telegram import Bot, Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler







# @csrf_exempt
# def telegram_bot(request):
#   if request.method == 'POST':
#     message = json.loads(request.body.decode('utf-8'))
#     chat_id = message['message']['chat']['id']
#     text = message['message']['text']
#     send_message("sendMessage", {
#       'chat_id': f'your message {text}'
#     })
#   return HttpResponse('ok')




# def send_message(method, data):
#   return requests.post(TELEGRAM_API_URL + method, data)




def setwebhook(request):
  response = requests.post(TELEGRAM_API_URL+ "setWebhook?url=" + URL).json()
  return HttpResponse(f"{response}")



@csrf_exempt
def telegram_bot(request):
    if request.method == 'POST':
        message = json.loads(request.body.decode('utf-8'))
        chat_id = message['message']['chat']['id']
        text = message['message']['text']
        send_message("sendMessage", {
            'chat_id': chat_id,
            'text': 'به ربات هوش مصنوعی قم بات خوش آمدید'
        })
    return HttpResponse('ok')

def send_message(method, data):
    url = f'{TELEGRAM_API_URL}{method}'
    response = requests.post(url, json=data)
    return response



TELEGRAM_BOT_TOKEN = TOKEN
bot = Bot(token=TELEGRAM_BOT_TOKEN)
update_queue = Queue()
updater = Updater(TELEGRAM_BOT_TOKEN, update_queue=update_queue)

@csrf_exempt
def new_start(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        chat_id = data['message']['chat']['id']
        username = data['message']['chat']['username']
        
        try:
            # Check if the user already exists
            user = User.objects.get(username=username)
            updater.bot.run_async(send_message, chat_id=chat_id, text='کاربر خوش آمدید!\nربات هوش مصنوعی قم بات آماده ارایه خدمات لبلینگ می باشد\nجهت ادامه دستور مربوطه را وارد فرمایید..', reply_markup=create_keyboard())
        except User.DoesNotExist:
            # Create a new user if it does not exist
            User.objects.create(
                id=chat_id,
                username=username,
            )
            updater.bot.run_async(send_message, chat_id=chat_id, text='ورود کاربر جدید\nبه ربات هوش مصنوعی قم بات خوش آمدید', reply_markup=create_keyboard())
        
        return HttpResponse('ok')
    return HttpResponse('Method not allowed', status=405)

def send_message(bot, update, chat_id, text, reply_markup=None):
    bot.send_message(chat_id=chat_id, text=text, reply_markup=reply_markup)

def create_keyboard():
    # Create inline keyboard with buttons
    keyboard = [
        [InlineKeyboardButton("Button 1", callback_data='button1')],
        [InlineKeyboardButton("Button 2", callback_data='button2')]
    ]
    return InlineKeyboardMarkup(keyboard)
















# @csrf_exempt
# def new_start(request):
#     if request.method == 'POST':
#         update = Update.de_json(json.loads(request.body.decode('utf-8')), bot=application.bot)
#         application.update_queue.put(update)
#         return HttpResponse('ok')
#     else:
#         return HttpResponse('Method not allowed', status=405)



# def new_start(update, context):
#     chat_id = update.message.chat_id
#     username = update.message.chat.username
#     # first_name = update.message.chat.first_name
#     # last_name = update.message.chat.last_name

#     # Check if the user already exists or create a new one
#     user, created = User.objects.get_or_create(
#         id=chat_id,
#         defaults={
#             # 'first_name': first_name,
#             # 'last_name': last_name,
#             'username': username
#         }
#     )

#     keyboard = [
#         [
#             InlineKeyboardButton("Button 1", callback_data='button1'),
#             InlineKeyboardButton("Button 2", callback_data='button2')
#         ]
#     ]
#     reply_markup = InlineKeyboardMarkup(keyboard)

#     update.message.reply_text(f"Hello, {username}!", reply_markup=reply_markup)




# def button(update, context):
#     query = update.callback_query
#     query.answer()

#     # Handle button press
#     if query.data == 'button1':
#         query.edit_message_text(text="Button 1 pressed")
#     elif query.data == 'button2':
#         query.edit_message_text(text="Button 2 pressed")

# # Add handlers to the application
# application.add_handler(CommandHandler('start', start))
# application.add_handler(CallbackQueryHandler(button))