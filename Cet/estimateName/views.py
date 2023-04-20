from django.shortcuts import render

def estName (request):
    return render(request, 'estimateName/estimate.html')