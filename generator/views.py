from django.shortcuts import render
import random
import generator
# from django.http import HttpResponse

# Create your views here.
def about(request):
    # return HttpResponse('Hello World Django')
    return render(request, 'generator/about.html')

def home(request):
    return render(request, 'generator/home.html')

def password(request):
    characters = list('abcdefghijklmnopqrstuvwxyz')
    generated_password = ''

    length = int(request.GET.get('length'))

    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

    if request.GET.get('special'):
        characters.extend(list('@!?-_#$%&/()'))
    
    if request.GET.get('numbers'):
        characters.extend(list('1234567890'))
    
    for x in range(length):
        generated_password += random.choice(characters)


    return render(request, 'generator/password.html', {'password': generated_password})
