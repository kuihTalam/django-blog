from __future__ import unicode_literals
from django.utils import timezone
from django.db import models

class Post(models.Model):
    author = models.ForeignKey('auth.User') # what is this?
    title = models.CharField(max_length=200) # is a character field and limit to max length of 200
    text = models.TextField() # is a text field
    created_date = models.DateTimeField(default=timezone.now) # point to current timezone
    published_date = models.DateTimeField(blank=True, null=True) # It's alright with empty/no published date, why?
    
    def publish(self):
        self.published_date = timezone.now()
        self.save()
        
    def __str__(self):
        return self.title