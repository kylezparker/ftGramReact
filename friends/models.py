import random 
from django.db import models

# Create your models here.
class Share(models.Model):
    # maps to sql data
    content = models.TextField(blank=True, null=True)
    image= models.FileField(upload_to='images/', blank=True, null=True)

    class Meta:
        ordering = ['-id']
        
    def serialize(self):
        return {
            "id":self.id,
            "content":self.content,
            "likes": random.randint(0,299)
        }