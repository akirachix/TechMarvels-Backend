from django.db import models
from wezeshaWebPortalCooperative.models import Cooperative

class Farmer(models.Model):
    farmer_id = models.SmallIntegerField(primary_key=True, default=1)
    farmer_first_name = models.CharField(max_length=20)
    farmer_last_name = models.CharField(max_length=20)
    farmer_email = models.EmailField()
    farmer_phone_number = models.CharField(max_length=20)
    farmer_password = models.CharField(max_length=20, default='defaultpassword')
    farmer_loan_status = models.CharField(max_length=20)
    cooperative_id = models.ForeignKey(Cooperative, on_delete=models.CASCADE, related_name='farmer_cooperative', default=1)


    def __str__(self):
        return f"{self.farmer_first_name} {self.farmer_last_name}"

