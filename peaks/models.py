from django.db import models
from django.core.validators import MaxValueValidator


class Peak(models.Model):
    name = models.CharField(max_length=255, help_text="Name of the peak.")
    altitude = models.PositiveSmallIntegerField(
        help_text="Altitude, in meters",
        validators=[
            MaxValueValidator(5000, "Are you sure this peak is located in Earth ?")
        ]
    )
    lat = models.FloatField()
    lon = models.FloatField()

    def __str__(self):
        return f"{self.pk}: {self.name}"
