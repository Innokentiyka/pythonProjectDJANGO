from django.shortcuts import render

def contacts(request):
    return render(request, 'main/contacts.html')

def home(request):
    return render(request, 'main/home.html')