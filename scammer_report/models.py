# Create your models here.
from django.db import models

# Define choices for telecom provider
TELECOM_PROVIDERS = [
    ('ais', 'AIS'),
    ('dtac', 'DTAC'),
    ('true', 'True'),
]

class ScammerReport(models.Model):
    reporter_name = models.CharField(max_length=100)
    scammer_phone = models.CharField(max_length=20)
    telecom_provider = models.CharField(
        max_length=10,
        choices=TELECOM_PROVIDERS,  # Use the choices parameter
        default='ais'  # Set a default value if you want
    )
    description = models.TextField()
    date_reported = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.reporter_name} reported {self.scammer_phone}"