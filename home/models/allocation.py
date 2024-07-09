from django.db import models
from .students import Student
from .period import Period
from .caterer import Caterer

class Allocation(models.Model):
    email = models.ForeignKey(
        Student, 
        default=0,
        on_delete=models.SET_NULL,
        null=True
    )
    student_id = models.CharField(
        default=None,
        max_length=30,
        null=True,
        blank=True,
    )
    period = models.ForeignKey(
        Period, 
        default=None, 
        on_delete=models.SET_NULL, 
        null=True
    )
    caterer = models.ForeignKey(
        Caterer, 
        default=None, 
        on_delete=models.SET_NULL, 
        null=True       
    )
    jain = models.BooleanField(
        default=False,null=True,blank=True
    )

    def __str__(self):
        return self.student_id

    class Meta:
        verbose_name = "Allocation Detail"
        verbose_name_plural = "Allocation Details"