"""
- Models inherit from django.db.models.Model class.
- Models class attributes represent database fields.
- class Meta within models is used to define medatada (example: name of the table.)
"""

from django.db import models
from django.urls import reverse
from django.utils import timezone

from todo_app.utils import one_week_later, ItemState


class ToDoList(models.Model):
    title = models.CharField(max_length=100, unique=True)
    
    def get_absolute_url(self):
        return reverse("list", args=[self.id])
    
    def __str__(self):
        return self.title


class ToDoItem(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField(default=one_week_later)
    state = models.TextField(choices=ItemState.choices, default=ItemState.TODO)
    todo_list = models.ForeignKey(ToDoList, on_delete=models.CASCADE)
    
    def get_absolute_url(self):
        return reverse("item-update", args=[str(self.todo_list.id), str(self.id)])
            
    def __str__(self):
        return f"{self.title} [{self.state}]: due {self.due_date}"
    
    class Meta:
        ordering = ["due_date"]
