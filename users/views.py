from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.forms import UserCreationForm

def logout_view(request):
    """Faz um Logout do usuario"""
    logout(request)
    return redirect('learning_logs:index')

def register(request):
    """Faz o cadastro de um novo usuário"""

    if request.user.is_authenticated:
        return redirect('learning_logs:index')

    if request.method != 'POST':
        # Exibe o formulario de cadastro em branco
        form = UserCreationForm()
    else:
        # Processa o formulario preenchido
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()
            # Faz login do usuario e o redireciona para a pagina inicial
            password = form.cleaned_data.get('password2')
            authenticated_user =  authenticate(username=new_user.username, password=password)
            login(request, authenticated_user)
            return redirect('learning_logs:index')
    
    context = {'form': form}
    return render(request, 'users/register.html', context)