from django.db import models
from wezeshaMobileApp.models import Farmer
from wezeshaWebPortalCooperative.models import Cooperative

class Saaco(models.Model):
    saaco_name = models.CharField(max_length=20)
    saaco_email = models.EmailField()
    saaco_phone_number = models.CharField(max_length=20)
    saaco_password = models.CharField(max_length=13, default='defaultpassword')
    farmer_id = models.ForeignKey(Farmer, on_delete=models.CASCADE, related_name='saaco_farmers', default=1)
    cooperative_id = models.ForeignKey(Cooperative, on_delete=models.CASCADE, related_name='saaco_cooperative', default=1)

    def __str__(self):
        return f"{self.saaco_name}"


