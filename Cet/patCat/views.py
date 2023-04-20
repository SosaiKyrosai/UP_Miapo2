from django.shortcuts import render

def pCat (request):
    return render(request, 'patCat/pat.html')