from django.shortcuts import render

# Create your views here.


import json
import requests
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

# from django_telegram_bot.settings import TELEGRAM_API_URL
from myapp.credentials import TELEGRAM_API_URL, URL, TOKEN
from myapp.models import User
import threading
import asyncio
from queue import Queue
# from django.utils.functional import async_to_sync

# from telegram import Bot, Update, InlineKeyboardButton, InlineKeyboardMarkup
# from telegram.ext import Updater, CommandHandler, CallbackQueryHandler





@csrf_exempt
def new_start(request):
    if request.method == ['POST']:
        data = json.loads(request.body.decode('utf-8'))
        chat_id = data['message']['chat']['id']
        username = data['message']['chat']['username']
    elif request.method == 'GET':
        
        try:
            from .tasks import sample_task
            # Check if the user already exists
            sig = sample_task.apply_async()

            
        except Exception:
            # Create a new user if it does not exist
            return HttpResponse('Im in Get Exception')        
        
        return HttpResponse('This is a GET request', status=200)
    else:

        return HttpResponse('Method not allowed', status=405)






























def setwebhook(request):
  response = requests.post(TELEGRAM_API_URL+ "setWebhook?url=" + URL).json()
  return HttpResponse(f"{response}")




'''
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

'''





