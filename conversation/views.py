from django.shortcuts import render , get_object_or_404
from item.models import Item
from django.shortcuts import redirect
from .models import Conversation
from .forms import ConversationMessageForm
from django.contrib.auth.decorators import login_required

@login_required
def new_conversation(request,item_pk):
    item = get_object_or_404(Item, pk=item_pk)
    if item.created_by== request.user:
        return redirect('dashboard:index') 

    conversations = Conversation.objects.filter(item=item).filter(members__in=[request.user.id])
    if conversations:
        return redirect('conversation:detail', pk=conversations.first().pk)
    
    if request.method == 'POST':
        form = ConversationMessageForm(request.POST)

        if form.is_valid():
            conversations = Conversation.objects.create(item=item)
            conversations.members.add(request.user)
            conversations.members.add(item.created_by)
            conversations.save()

            conversations_message = form.save(commit=False)
            conversations_message.conversation = conversations
            conversations_message.created_by = request.user
            conversations_message.save()
            return redirect('item:detail', pk=item_pk)
    else:
        form = ConversationMessageForm() 

    return render(request, 'conversation/new.html',{
        'form':form,
    })

@login_required
def inbox(request):
    conversations = Conversation.objects.filter(members__in=[request.user.id])
    return render(request, 'conversation/inbox.html',{
        'conversations':conversations,
    })

@login_required
def detail(request,pk):
    conversation = Conversation.objects.filter(members__in=[request.user.id]).get(pk=pk)

    if request.method == 'POST':
        form = ConversationMessageForm(request.POST)

        if form.is_valid():
            conversations_message = form.save(commit=False)
            conversations_message.conversation = conversation
            conversations_message.created_by = request.user
            conversations_message.save()
            conversation.save()

            return redirect('conversation:detail', pk=pk) 
    else:
        form = ConversationMessageForm()

    return render(request, 'conversation/detail.html',{
        'conversation':conversation,
        'form':form, 
    })