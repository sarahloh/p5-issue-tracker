from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

CATEGORY_CHOICES = (
    ('BUG', 'Bug'),
    ('FEATURE', 'Feature')
)

STATUS_CHOICES = (
    ('TODO', 'Todo'),
    ('DOING', 'Doing'),
    ('DONE', 'Done')
)

class Ticket(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=255)
    description = models.TextField()
    category = models.CharField(max_length=7, choices=CATEGORY_CHOICES, default='BUG')
    status = models.CharField(max_length=255, choices=STATUS_CHOICES, default='TODO')
    upvotes = models.IntegerField(default=0)
    created_date = models.DateTimeField(auto_now_add=True)
    last_modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title