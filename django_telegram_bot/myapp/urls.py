from django.urls import path
from . import views

urlpatterns = [
  path('start/', views.new_start, name='start'),
  path('setwebhook/', views.setwebhook, name='setwebhook'), #new
]