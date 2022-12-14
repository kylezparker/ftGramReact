"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from friends.views import (
    share_action_view,
    share_delete_view,
    home_view, 
    share_detail_view, 
    share_list_view,
    share_create_view,
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view),
    path('create-share', share_create_view),
    path('friends', share_list_view),
    path('api/friends/action', share_action_view),
    path('api/friends/<int:share_id>/delete', share_delete_view),
    path('friends/<int:share_id>', share_detail_view),
    # path('api/friends/', include('friends.urls')),
]
