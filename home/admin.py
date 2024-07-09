from django.contrib import admin
from .models import Contact, Cafeteria, Caterer, Student, longRebate, Rule, Allocation, Period, shortRebate, Forms, Semester
from .models.messperiod import messPeriod

# Register your models here.
admin.site.register(Contact)
admin.site.register(Cafeteria)
admin.site.register(Caterer)
admin.site.register(Period)
admin.site.register(Student)
admin.site.register(longRebate)
admin.site.register(Rule)
admin.site.register(Allocation)
admin.site.register(shortRebate)
admin.site.register(messPeriod)
admin.site.register(Forms)
admin.site.register(Semester)