from django.db import models

class Farmer(models.Model):
    farmer_first_name = models.CharField(max_length = 20)
    farmer_last_name = models.CharField(max_length = 20)
    farmer_email= models.EmailField()
    farmer_phone_number = models.CharField(max_length = 20)
    farmer_loan_status = models.CharField(max_length = 20)
    image = models.ImageField()


    def __str__(self):
        return f"{self.first_name} {self.last_name}"
