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

def hipotenusa(request):
    return render(request, 'generator/hipotenusa.html')

def tuhipotenusa(request):
    def calculateHipotenusa(catetoa, catetob):
        catetoa = catetoa ** 2
        catetob = catetob ** 2
        catetoc = (catetoa + catetob) ** 0.5
        return round(catetoc, 2)
    
    catetoa = int(request.GET.get('catetoa'))
    catetob = int(request.GET.get('catetob'))
    catetoA2 = catetoa**2
    catetoB2 = catetob**2 
    cateto_suma = catetoB2 + catetoA2

    hipotenusa = calculateHipotenusa(catetoa, catetob)
    
    
    return render(request, 'generator/turesultado.html', {'hipotenusa': hipotenusa, 'catetoa': catetoa, 'catetob': catetob, 'catetoA': catetoA2, 'catetoB': catetoB2, 'catetoS': cateto_suma})
