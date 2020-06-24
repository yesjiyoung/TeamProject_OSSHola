from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.list import ListView
from django.urls import reverse

from .models import Video
#[JY]About User 
from django.contrib.auth.models import User  
from django.contrib import auth, messages #messages for video_like
from django.contrib.auth import get_user_model
User = get_user_model()


# [HS]About video_like
from django.views.decorators.http import require_POST
from django.http import HttpResponse, HttpResponseRedirect
import json

#[JY]About comment
from .models import Comment
from .forms import *


class VideoLoad(ListView):
    model=Video
    def get(self, request):
        template_name='home.html'
        AIList = Video.objects.filter(tag="인공지능운동")
        VideoList = Video.objects.all()
        return render(request, template_name, {'AIList':AIList, 'VideoList':VideoList})


class AiLoad(ListView):
    model=Video
    def get(self, request):
        template_name='ai_home.html'
        AIList = Video.objects.filter(tag="인공지능운동")

        return render(request, template_name, {'AIList':AIList})

def detail(request, detail_id):
    detail_obj = get_object_or_404(Video, pk=detail_id)

    if request.method == "POST":
        comment_form = CommentForm(request.POST or None)
        #comment_form.instance.user_id = request.user.id
        #comment_form.instance.v_id = v_id

        if comment_form.is_valid():
            #comment = comment_form.save()
            content = request.POST.get('content')
            comment = Comment.objects.create(video=detail_obj, user=request.user, content=content)
            comment.save()
            return HttpResponseRedirect(reverse('detail', args=(detail_obj.id)))
            #return redirect('detail')

    comment_form = CommentForm()
    comments = detail_obj.comments.all()

    return render(request, 'detail_be.html', {'detailObj':detail_obj, "comments":comments, "comment_form":comment_form})

def ai_detail(request, ai_detail_id):
    detail_ai_obj = get_object_or_404(Video, pk=ai_detail_id)
    return render(request, 'Ai_detail.html', {'detail_ai_obj':detail_ai_obj})

@require_POST
def video_like(request):
    pk = request.POST.get('pk',None)
    video = get_object_or_404(Video, pk=pk)
    video_like, video_like_created = video.like_set.get_or_create(user=request.user)
    # get_or_create는 (꺼내려는 모델의 인스턴스, boolean flag)를 튜플 형식으로 반환한다.
    
    if not video_like_created:
        # video_like_created가 FALSE일때, 기존 DB에 이미 인스턴스가 있는 상태니까 이미 눌러진 좋아요를 삭제한다.
        video_like.delete()
        message="좋아요 취소"
    else:
        # video_like_created가 TRUE일때, 좋아요 상태가 아니었고, 좋아요를 할거다.
        message = "좋아요"
    context={'like_count':video.like_count,
    'message': message} # 'nickname':request.user.profile.닉네임 context로 추가 예정

    return HttpResponse(json.dumps(context), content_type='application/json') #context를 json타입으로 보낸다)



def signup(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            user = User.objects.create_user(
                username=request.POST['username'],
                password=request.POST['password1'], 
                nickname=request.POST['nickname'],
                age=request.POST['age'],
                workingout=request.POST['workout_data']
                )
            auth.login(request, user)
            return redirect('correct')
        else:
            return redirect('uncorrect')
    return render(request, 'signup.html')

def correct(request):
    return render(request, 'signup_correct.html')

def uncorrect(request):
    return render(request, 'signup_uncorrect.html')



def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'unlog_be.html')
    else:
        return render(request, 'login_be.html')

def unlog(request):
    return render(request, 'unlog.html')


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('home')
    return render(request, 'home.html')












