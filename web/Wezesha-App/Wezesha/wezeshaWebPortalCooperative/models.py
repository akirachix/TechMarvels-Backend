from django.db import models

class Cooperative(models.Model):
    cooperative_id = models.SmallIntegerField(primary_key=True, default=1)
    cooperative_name = models.CharField(max_length=20)
    cooperative_email = models.EmailField()
    cooperative_phone_number = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.cooperative_name}"


