from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField()
    pos = models.CharField(max_length=255, blank=True)  # New field for position
    phone_number = models.CharField(max_length=12, blank=True)

    def __str__(self):
        return self.name