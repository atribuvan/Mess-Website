from django.db import models
from .caterer import Caterer
from .semester import Semester
from .messperiod import messPeriod

class Student(models.Model):
    name = models.CharField(
        max_length=100,
        null=True,
        default="",
        blank=True,
    )
    email = models.CharField(
        max_length=50, 
        default=""
    )
    caterer_alloted = models.ForeignKey(
        Caterer, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True
    )
    semester = models.ForeignKey(
        Semester, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True
    )
    mess_period = models.ForeignKey(
        messPeriod, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True
    )
    alloted_id = models.CharField(
        max_length=20,
        default="",
        blank=True,
    )
    roll_no = models.CharField(     
        max_length=20,
        default="",
        blank=True,
    )
    rebate_amount = models.IntegerField(
        default=0,
        null=True
    )
    total_fees = models.IntegerField(
        default=16000,
        null=True
    )
    shortrebate_days = models.IntegerField(
        default=0,
        null=True
    )
    longrebate_days = models.IntegerField(
        default=0,
        null=True
    )

    def __str__(self):
        return str(self.email)

    class Meta:
        verbose_name = "Student Details"
        verbose_name_plural = "Student Details"


