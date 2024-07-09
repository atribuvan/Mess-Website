from django.db import models

class Cafeteria(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    phone_number = models.CharField(max_length=12, blank=True)
    image = models.ImageField(upload_to='cafeteria_images/', blank=True)  

    def __str__(self):
        return self.name