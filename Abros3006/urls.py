"""
URL configuration for Abros3006 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.shortcuts import redirect
from django.contrib.auth.views import LogoutView
# from django.contrib.auth.views import Login

# Import views from your apps
from home import views as home_views
from snapshots import views as snapshots_views
from blog import views as blog_views
from users import views as users_views

from django.conf import settings
from django.conf.urls.static import static

def redirect_to_oauth_login(request):
    return redirect('/accounts/login')  # Replace with your OAuth URL
def redirect_to_oauth_logout(request):
    return redirect('/')  # Replace with your OAuth URL

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Home app
    path('', home_views.home, name='home'),
    
    # Blog app
    path('blog/', blog_views.blog, name='blog'),

    # resume app
    path('resume/', home_views.resume, name='resume'),

    #snapshots
    path('snapshots/', snapshots_views.snapshots, name='snapshots'),

    #Post
    path('blog/<str:post_id>/', blog_views.post, name='post'),

    # User authentication
    path('accounts/', include('allauth.urls')),

    path('login/', redirect_to_oauth_login, name='login'),
    
    path('logout/', users_views.logout_view, name='logout'),
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)