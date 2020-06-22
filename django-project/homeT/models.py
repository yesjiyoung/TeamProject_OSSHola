from django.conf import settings
from django.db import models
        
class Video(models.Model):
    title = models.CharField(max_length=200)
    # description = models.TextField(blank=True, null=True)
    # image = models.ImageField(upload_to='video_thumbnails/%Y/%m/%d')
    v_id = models.CharField(max_length=140, help_text="youtube 영상 코드를 입력해주세요")
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    like_user_set = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name='like_user_set',through='Like') 

    @property
    def like_count(self):
        return self.like_user_set.count()

    class Meta:
        ordering=['-created_at']

    def __str__(self):
        return self.title


class Like(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)

    

