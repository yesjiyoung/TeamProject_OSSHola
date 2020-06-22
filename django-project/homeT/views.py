from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Video

#[JY]About User 
from django.contrib.auth.models import User  
from django.contrib import auth  

# Create your views here.



class VideoLoad(ListView):
    model = Video

    def get(self,request):
        template_name = 'home_be.html'
        VideoList = Video.objects.all()
        return render(request, template_name, {'VideoList':VideoList})



def signup(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
            auth.login(request, user)
            return redirect('correct')
        else:
            return redirect('uncorrect')
    return render(request, 'signup.html')




