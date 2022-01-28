# chat/views.py
from email import message
from django.shortcuts import render
from .models import ChatModel


def index(request):
    return render(request, 'chat/index.html', {})


def room(request, room_name):

    chat_model_qs = ChatModel.objects.filter(room_no=room_name)

    message_list = []

    for chat_model_obj in chat_model_qs:
        message_list.append(chat_model_obj.message)

    print(message_list)

    return render(request, 'chat/room.html', {
        'room_name': room_name,
        'messages': message_list
    })
