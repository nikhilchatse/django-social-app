from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class posts(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    image=models.FileField(upload_to='posts',null=True,blank=True)
    captions=models.CharField(max_length=500)
    created_at=models.DateTimeField(auto_now_add=True)
    likes=models.ManyToManyField(User,related_name='post_likes',blank=True)

    def total_likes(self):
        return self.likes.count()
    

class Comment(models.Model):
    post = models.ForeignKey(posts, on_delete=models.CASCADE, related_name="comments")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
