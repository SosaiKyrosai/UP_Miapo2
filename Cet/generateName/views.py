from django.shortcuts import render

def generName (request):
    return render(request, 'generateName/generate.html')
