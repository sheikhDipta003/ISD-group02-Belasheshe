from django.db import models
from residents.models import CheckupItem, Member
from doctors.models import Doctor

# Create your models here.
class Nurse(models.Model):
    Nurse_Id = models.AutoField(primary_key=True)
    Qualifications = models.CharField(max_length=50)
    Shift = models.CharField(max_length=20)

    def __str__(self):
        return f"Checkup {self.Nurse_Id}"
    
class CheckupSchedule(models.Model):
    Checkup_id=models.OneToOneField(CheckupItem, primary_key=True, on_delete=models.CASCADE)
    Member_Id = models.ForeignKey(Member, on_delete=models.CASCADE)
    Nurse_Id = models.ForeignKey(Nurse, on_delete=models.CASCADE)
    Doctor_Id = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    Date = models.DateField()
    Completed = models.BooleanField(default=False)

    def __str__(self):
        return f"Checkup Schedule for {self.Checkup_id}"

class SpecialCheckupSchedule(models.Model):
    Special_Checkup_Id = models.OneToOneField(CheckupItem, primary_key=True, on_delete=models.CASCADE)
    Member_Id = models.ForeignKey(Member, on_delete=models.CASCADE)
    Nurse_Id = models.ForeignKey(Nurse, on_delete=models.CASCADE)
    Doctor_Id = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    Date = models.DateField()
    Frequency = models.PositiveIntegerField()
    Completed = models.BooleanField(default=False)

    def __str__(self):
        return f"Special Checkup Schedule for {self.Special_Checkup_Id}"
