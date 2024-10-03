from django.shortcuts import render
from chat.models import Message
from chat.models import Chat

def index(request):
    if request.method == 'post':            
        print("Request method is post" + request.POST['textmessage'])        
        #testChat = Chat.objects.get(id=1)        
        #Message.objects.create(text=request.POST['textmessage'], chat=testChat, author=request.user, receiver=request.user)    
    
    #chat_messages = Message.objects.filter(chat__id=1)    
    
    return render(request, 'chat/index.html', {'username': 'yannickvaterlaus'})
