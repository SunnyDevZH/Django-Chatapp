from django.shortcuts import render
from chat.models import Message
from chat.models import Chat
from django.http.response import HttpResponseRedirect
from django.contrib.auth import authenticate, login

def index(request):
    if request.method == 'post':            
        print("Request method is post" + request.POST['textmessage'])        
        #testChat = Chat.objects.get(id=1)        
        #Message.objects.create(text=request.POST['textmessage'], chat=testChat, author=request.user, receiver=request.user)    
    
    #chat_messages = Message.objects.filter(chat__id=1)    
    
    return render(request, 'chat/index.html', {'username': 'yannickvaterlaus'})

def login_view(request):
    if request.method == 'post': 
        user = authenticate(username=request.Post.get('username'), password=request.Post.get('password'))
        if user:
            login(request, user)
            return HttpResponseRedirect('/chat/')
        else:
            return render(request, 'auth/login.html', {'wrongPasswort': True})
    return render(request, 'auth/login.html')
