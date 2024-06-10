from django.shortcuts import render

# Create your views here.


import json
import requests
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
# from django_telegram_bot.settings import TELEGRAM_API_URL
from myapp.credentials import TELEGRAM_API_URL, URL
from myapp.models import User

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



@csrf_exempt
def start(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        chat_id = data['message']['chat']['id']
        username = data['message']['chat']['username']
        # first_name = data['message']['chat']['first_name']
        # last_name = data['message']['chat']['last_name']
        
        try:
            # Check if the user already exists
            user = User.objects.get(username=username)
            # user_profile = user.profile  # Assuming a one-to-one relationship with a profile model if needed
            send_message("sendMessage", {
            'chat_id': chat_id,
            'text': f"کاربر {user.username}\nخوش آمدید!\nربات هوش مصنوعی قم بات آماده ارایه خدمات لبلینگ می باشد\nجهت ادامه دستور مربوطه را وارد فرمایید.."
                })
        except User.DoesNotExist:
            # Create a new user if it does not exist
            user = User.objects.get_or_create(
                id = chat_id,
                username=username,
                # first_name=first_name,
                # last_name=last_name,
                
            )
            send_message("sendMessage", {
            'chat_id': chat_id,
            'text': 'ورود کاربر جدید\nبه ربات هوش مصنوعی قم بات خوش آمدید'
                })
        
        # Process the message as needed
        response_text = f"Hello, {user.id}!" if id else "Hello!"
        
        return JsonResponse({'message': response_text})
    return HttpResponse('ok')