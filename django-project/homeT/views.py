from django.shortcuts import render

# Create your views here.
class VideoLoad(ListView):
    model = Video

    def get(self,reqest):
        template_name = 'home_be.html'
        VideoList = Video.objects.all()
        return render(request, template_name, {'VideoList':VideoList})