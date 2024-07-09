from django.db import models

class Caterer(models.Model):
    name = models.CharField(
        max_length=50,
        unique=True
    )
    student_limit = models.IntegerField(
        default=0
    )
    current_no_students = models.IntegerField(
        default=0,
        null=True
    )
    email = models.EmailField( 
        max_length=254,
        default=""
    )
    visible = models.BooleanField(
        default=False,
        null=True
    )
    amount_tobe_paid = models.IntegerField(
        default=0,
        null=True
    )
    rebate_rate = models.IntegerField(
        default=160,
        null=True
    )
    id_tobe_alloted = models.CharField(
        max_length=20,
        default="",
        blank=True,
    )
    image = models.ImageField(upload_to='caterer_images/', blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Caterer"
        verbose_name_plural = "Caterers"