from django.db import models
from .shortrebate import shortRebate
from .caterer import Caterer
from .messperiod import messPeriod

class Period(models.Model):
    email = models.CharField(max_length=50, default="")
    start_date = models.DateField()
    end_date = models.DateField()
    mess_period = models.ForeignKey(messPeriod, on_delete=models.SET_NULL, null=True, blank=True)
    short_rebates = models.ForeignKey(shortRebate, related_name='period_short_rebates', blank=True, on_delete=models.SET_NULL, null=True)
    caterer = models.ForeignKey(Caterer, on_delete=models.SET_NULL, null=True, blank=True)
    
    def __str__(self):
        return f"{self.start_date} to {self.end_date}"

    @property
    def total_short_rebate_amount(self):
        return sum(rebate.amount for rebate in self.short_rebates.all())

    @property
    def total_long_rebate_amount(self):
        return sum(rebate.days * rebate.email.caterer_alloted.rebate_rate for rebate in self.long_rebates.all())
    
    class Meta:
        verbose_name = "Period"
        verbose_name_plural = "Periods"