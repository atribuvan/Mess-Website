from django.db import models

class Semester(models.Model):
    name = models.CharField(
        max_length=50,
        blank=True,
        null=True
    )
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Semester"
        verbose_name_plural = "Semesters"