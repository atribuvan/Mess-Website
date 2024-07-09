from django.db import models

class Forms(models.Model):
    title = models.CharField(
        max_length=250,
        unique=True
    )
    description = models.TextField(
        blank=True
    )
    link = models.URLField(
        max_length=500
    )

    def __str__(self):
        return "Form " + self.title

    class Meta:
        verbose_name = "Form"
        verbose_name_plural = "Forms"