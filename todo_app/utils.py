from django.db import models
from django.utils import timezone


def one_week_later():
    return timezone.now() + timezone.timedelta(days=7) 


class ItemState(models.TextChoices):
    DONE = "Done"
    # ENDS_SOON = "ENDS SOON"
    IN_PROGRESS = "In Progress"
    TODO = "To Do"
    INCOMPLETE = "Incomplete" 