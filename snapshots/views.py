from django.shortcuts import render
from .models import Story
import os
from django.conf import settings
from django.contrib.auth.decorators import login_required


# @login_required
def snapshots(request):
    stories = Story.objects.all().order_by('-id')
    images_dir = os.path.join(settings.BASE_DIR, 'static', 'snapshot_images')
    
    for story in stories:
        image_path = f'snapshot{story.id}_image{story.id}.jpg'
        full_image_path = os.path.join(images_dir, image_path)
        
        if os.path.exists(full_image_path):
            story.image_url = f'snapshot_images/{image_path}'
        else:
            story.image_url = None  # Or a default image URL

    return render(request, 'snapshots.html', {'stories': stories})