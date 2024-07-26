from django.shortcuts import render
from .models import Story
# Create your views here.

def snapshots(request):
    storys = Story.objects.all()
    return render(request, 'snapshots.html', {'storys':storys})
