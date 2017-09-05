# todo/models.py
from __future__ import unicode_literals

from django.db import models

class ToDoList(models.Model):
    title = models.CharField(max_length=100)
    
class ToDoListItem(models.Model):
    todo_list = models.ForeignKey(
        'ToDoList',
        related_name='items', on_delete=models.CASCADE
    )
    
    title = models.CharField(max_length=100)
    
    description = models.TextField(blank=True, default='')