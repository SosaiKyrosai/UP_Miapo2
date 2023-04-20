from django.shortcuts import render

def arrCats (request):
    return render(request, 'arrangeTheCats/arrange.html')