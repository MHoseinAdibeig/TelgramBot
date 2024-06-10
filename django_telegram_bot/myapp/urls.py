from django.urls import path
from . import views

urlpatterns = [
  path('start/', views.start, name='start'),
  path('setwebhook/', views.setwebhook, name='setwebhook'), #new
]