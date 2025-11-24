from django.db import models
class SubscribedUser(models.Model):
    mail = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.mail
# Create your models here.
