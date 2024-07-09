from django.db import models
from .semester import Semester

class messPeriod(models.Model):
    start_date = models.DateField()
    end_date = models.DateField()
    semester=models.ForeignKey(
        Semester, 
        on_delete=models.SET_NULL, 
        null=True
    )
    allotment = models.BooleanField(
        default=False
    )

    def __str__(self):
        return f"{self.start_date} to {self.end_date}"

    class Meta:
        verbose_name = "Mess Period"
        verbose_name_plural = "Mess Periods"