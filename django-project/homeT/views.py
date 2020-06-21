from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Video
# Create your views here.


class VideoLoad(ListView):
    model = Video

    def get(self,request):
        template_name = 'home_be.html'
        VideoList = Video.objects.all()
        return render(request, template_name, {'VideoList':VideoList})