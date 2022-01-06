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

