from django.db import models


class Subscriber(models.Model):
    email = models.EmailField(unique=True)
    date_subscribed = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email

class Newsletter(models.Model):
    subject = models.CharField(max_length=200)
    content = models.TextField()
    sent_at = models.DateTimeField()

    def __str__(self):
        return self.subject