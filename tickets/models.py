from django.db import models

class Ticket(models.Model):
    user_id = models.IntegerField()
    title = models.CharField(max_length=255)
    description = models.TextField()
    type = models.CharField(max_length=255)
    status = models.CharField(max_length=255)
    upvotes = models.IntegerField()

    def __str__(self):
        return self.title