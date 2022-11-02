import random 
from django.conf import settings
from django.db import models

User = settings.AUTH_USER_MODEL
# Create your models here.

class ShareLike(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    share = models.ForeignKey("Share", on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

class Share(models.Model):
    # maps to sql data
    user = models.ForeignKey(User, on_delete=models.CASCADE) # many users can own many tweets
    likes = models.ManyToManyField(User, related_name='share_user', blank=True, through=ShareLike )
    content = models.TextField(blank=True, null=True)
    image = models.FileField(upload_to='images/', blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content

    class Meta:
        ordering = ['-id']

    def serialize(self):
        return {
            "id":self.id,
            "content":self.content,
            "likes": random.randint(0,299)
        }