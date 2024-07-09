from django.db import models
from .students import Student
from .semester import Semester 
import datetime

class longRebate(models.Model):
    student = models.ForeignKey(
        Student,
        on_delete=models.SET_NULL,
        null=True, 
        blank=True
    )
    start_date = models.DateField(
        null=True, 
        blank=True
    )
    end_date = models.DateField(
        null=True, 
        blank=True
    )   
    days = models.IntegerField(
        default=8
    )
    approved = models.BooleanField(
        default=False
    )
    amount = models.IntegerField(
        null=True,
        blank=True
    )
    semester = models.ForeignKey(
        Semester,
        on_delete=models.SET_NULL,
        null=True, 
        blank=True
    )
    date_applied = models.DateField(
        default=datetime.date.today
    )
    file = models.FileField(upload_to="documents/", default=None, null=True, blank=True)

    def __str__(self):
        return str(self.date_applied) +" "+ str(self.student.email)

    class Meta:
        verbose_name = "Long Rebate Details"
        verbose_name_plural = "Long Rebate Details"