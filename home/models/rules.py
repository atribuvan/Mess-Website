from django.db import models

class Rule(models.Model):
    sno = models.AutoField(primary_key=True)  # Corrected typo (lowercase 's')
    rule_text = models.TextField(default="")  # Improved field name for clarity
    order = models.IntegerField(blank=True, null=True)  # Optional field for sorting

    class Meta:
        verbose_name = "Rule"
        verbose_name_plural = "Rules"