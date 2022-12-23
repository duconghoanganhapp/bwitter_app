from django.db import models
from django.contrib.auth import get_user_model
import uuid
from datetime import datetime

User = get_user_model()

# Create your models here.
class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_user = models.IntegerField()
    bio = models.TextField(blank=True)
    profileimg = models.ImageField(upload_to='profile_images', default='blank-profile-picture.png')
    location = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.user.username

class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    user = models.CharField(max_length=100)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='post_images')
    caption = models.TextField()
    created_at = models.DateTimeField(default=datetime.now)
    no_of_likes = models.IntegerField(default=0)
    #number_of_comments = models.IntegerField(default=0)
    
    def __str__(self):
        return self.user

class LikePost(models.Model):
    post_id = models.CharField(max_length=500)
    username = models.CharField(max_length=100)

    def __str__(self):
        return self.username

class FollowersCount(models.Model):
    follower = models.CharField(max_length=100)
    user = models.CharField(max_length=100)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    def __str__(self):
        return self.user

class Comment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    caption = models.CharField(max_length=100)
    image = models.ImageField(upload_to='cmt_images')

    def __str__(self):
        return self.caption


# class Conversation(models.Model):
#     id = models.UUIDField(primary_key=True, default=uuid.uuid4)
#     profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
#     user_rep = models.ForeignKey(User, on_delete=models.CASCADE)
#     created_at = models.DateTimeField(default=datetime.now)

#     def __str__(self):
#         return self.created_at

class Message(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    user_rep = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.CharField(max_length=100)
    image = models.ImageField(upload_to='cmt_images')
    # conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.content
