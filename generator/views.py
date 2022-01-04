from django.shortcuts import render
import random
import generator

# Create your views here.
def about(request):
    # return HttpResponse('Hello World Django')
    return render(request, 'generator/about.html')
