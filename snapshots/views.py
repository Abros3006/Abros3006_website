from django.shortcuts import render

# Create your views here.

def snapshots(request):
    return render(request, 'snapshots.html')
