from django.db import models
from .students import Student
from .caterer import Caterer
from .messperiod import messPeriod
from .semester import Semester
import datetime
from django.core.exceptions import ValidationError

class shortRebate(models.Model):
    student_applied = models.ForeignKey(
        Student, 
        on_delete=models.SET_NULL, 
        null=True, 
        verbose_name="Student Email"
    )
    rebating_caterer = models.ForeignKey(
        Caterer,
        related_name="caterer",
        on_delete=models.SET_NULL,
        null=True
    )
    start_date = models.DateField()
    end_date = models.DateField()
    days_applied = models.IntegerField(
        default=2,
        # max=8
    )
    date_applied = models.DateField(
        default=datetime.date.today
    )
    amount = models.IntegerField(
        null=True
    )
    mess_period = models.ForeignKey(
        messPeriod, 
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

    def clean(self):
        # Check if start_date and end_date are provided
        if not self.start_date or not self.end_date:
            raise ValidationError("Both start date and end date are required.")

        # Check if start_date and end_date are consecutive days
        if (self.end_date - self.start_date).days != 1:
            raise ValidationError("Short term rebate should be applied for 2-7 consecutive days.")

        # Check if the rebate days exceed the maximum limit of 8 days/month
        if self.mess_period:
            total_days = shortRebate.objects.filter(
                student_applied=self.student_applied,
                mess_period=self.mess_period
            ).aggregate(total_days=models.Sum(models.F('end_date') - models.F('start_date')))['total_days']
            
            if total_days and total_days + 1 > 8:  # +1 because we are including the current rebate
                raise ValidationError("Maximum of 8 days/month of rebate can be availed.")

    def __str__(self):
        return f"{self.student_applied.name} | {self.start_date} to {self.end_date}"
    class Meta:
        verbose_name = "Short Rebate Details"
        verbose_name_plural = "Short Rebate Details"