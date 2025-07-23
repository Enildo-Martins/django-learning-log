from django.shortcuts import render, redirect
from .models import Topic, Entry
from .forms import TopicForm, EntryForm


def index(request):
    """Pagina principal do Learning_Log"""
    return render(request, 'learning_logs/index.html')

def topics(request):
    """Mostra todos os assuntos"""
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)

def topic(request, topic_id):
    """Mostra um único assunto e todas as suas entradas"""
    topic = Topic.objects.get(id = topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)

def new_topic(request):
    """Adiciona um novo assunto."""
    if request.method != 'POST': 
        # Nenhum dado submetido, cria um formulario em branco
        form = TopicForm()
    else:
        # Dados de POST submetidos, processa os dados.
        form = TopicForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('learning_logs:topics')
    context = {'form' : form}
    return render(request, 'learning_logs/new_topic.html', context)

def new_entry(request, topic_id):
    """Acrescenta uma nova entrada para um assunto em particular."""
    topic = Topic.objects.get(id=topic_id)

    if request.method != 'POST':
        form = EntryForm()
    else:
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return redirect('learning_logs:topic', topic_id=topic.id) 
    context = {'topic':topic, 'form':form}
    return render(request, 'learning_logs/new_entry.html', context)

def edit_entry(request, entry_id):
    """Edita uma entrada ja existente"""
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic

    if request.method != 'POST':
        form = EntryForm(instance=entry)
    else:
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('learning_logs:topic', topic_id=topic.id)

    context = {'entry': entry, 'topic': topic, 'form':form}
    return render(request, 'learning_logs/edit_entry.html', context)

def delete_entry(request, entry_id):
    """Exclui uma entrada ja existente"""
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic

    if request.method == 'POST':
        #Se o usuario confirmou no formulario, deleta o objeto
        entry.delete()
        return redirect('learning_logs:topic', topic_id=topic.id)

    context = {'entry': entry, 'topic': topic}
    return render(request, 'learning_logs/delete_entry.html', context)