from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import logout

def logout_view(request):
    """Faz um Logout do usuario"""
    logout(request)
    return redirect('learning_logs:index')