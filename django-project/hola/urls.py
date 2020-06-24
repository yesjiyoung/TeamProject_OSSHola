"""hola URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path

import homeT.views
#[JY] User Model 작업때문에 잠시 주석처리합니다. -> 다시 살림
from homeT.views import VideoLoad, video_like,detail

urlpatterns = [
    path('', VideoLoad.as_view(), name='home'),
    path('detail/<int:detail_id>', homeT.views.detail, name='detail'),
    path('detail/$', homeT.views.video_like, name='video_like'),
    path('admin/', admin.site.urls),
    path('signup/', homeT.views.signup, name='signup'),
    path('unlog/', homeT.views.unlog, name='unlog'),
    path('login/', homeT.views.login, name='login'),
    path('logout/', homeT.views.logout, name='logout'),
    path('correct/', homeT.views.correct, name = 'correct'),
    path('uncorrect/', homeT.views.uncorrect, name = 'uncorrect'),
    
]
