from django.shortcuts import render

# Create your views here.
def harry(request):
    return render(request,'harry.html')

def hermione(request):
    return render(request,'hermione.html')

def ron(request):
    return render(request,'ron.html')