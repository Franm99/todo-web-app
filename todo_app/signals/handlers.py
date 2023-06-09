from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils import timezone
from django.db.models import Q

from todo_app.models import ToDoItem
from todo_app.utils import ItemState


@receiver(pre_save, sender=ToDoItem)
def get_state_from_date(sender, instance:ToDoItem, **kwargs):
    
    if instance.due_date < timezone.now() and instance.state != 'DONE':
            instance.state = ToDoItem.STATE_INCOMPLETE
