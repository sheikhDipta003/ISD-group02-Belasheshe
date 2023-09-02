from django.db import models
#from staff.models import Staff

# Create your models here.
class Doctor(models.Model):
    Doctor_ID=models.AutoField(primary_key=True, max_length=10)
    Name=models.CharField(max_length=100)
    Qualifications = models.CharField(max_length=100)
    Shift = models.CharField(max_length=50)
    #Staff_ID=models.ForeignKey(Staff, on_delete=models.CASCADE)

    def __str__(self):
        return self.Name