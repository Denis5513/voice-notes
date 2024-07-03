from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def authorization_required(request):
    return render(request, 'authorization_message.html')
