from django.db import models
# from django.shortcuts import resolve_url

# Create your models here.
# class Category(models.Model):
#     parent_category = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True, related_name='sub_categories')
#     name = models.CharField(max_length=200) # category 이름
#     description = models.TextField(max_length=200) # 간단 설명
#     slug = models.SlugField(max_length=200, allow_unicode=True, unique=True)
#     def __str__(self):
#         return self.name
#     class Meta:
#         ordering=['name']
#     def get_absolute_url(self):
#         return resolve_url('product_in_category', self.slug)
        
class Video(models.Model):
    title = models.CharField(max_length=200)
    # description = models.TextField(blank=True, null=True)
    # image = models.ImageField(upload_to='video_thumbnails/%Y/%m/%d')
    v_id = models.CharField(max_length=140, help_text="youtube 영상 코드를 입력해주세요")
    created_at = models.DateTimeField(auto_now_add=True, blank=True)

    class Meta:
        ordering=['-created_at']

    def __str__(self):
        return self.title

    

