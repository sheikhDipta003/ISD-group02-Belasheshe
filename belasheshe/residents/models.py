from django.db import models
# from viewflow.fields import CompositeKey
# from healthcare.models import ResidentRoomAsgn, Doctor, Nurse, MedCond
# from .member import Member
# from nurse.models import MedicineChart,Medicine
#from doctors.models import Doctor




class MedCond(models.Model):
    Cond_ID=models.AutoField(primary_key=True)
    Name=models.CharField(max_length=50)
    Advice=models.CharField(max_length=150)
    Guideline=models.CharField(max_length=150)
    


class CheckupItem(models.Model):
    Checkup_Id = models.AutoField(primary_key=True)
    Blood_Pressure = models.CharField(max_length=20)
    Sugar = models.DecimalField(max_digits=5, decimal_places=2)
    Heartrate = models.IntegerField()

    def __str__(self):
        return f"Checkup {self.Checkup_Id}"

# class SpecialCheckupSchedule(models.Model):
#     Special_Checkup_Id = models.OneToOneField(CheckupItem, primary_key=True, on_delete=models.CASCADE)
#     Member_Id = models.ForeignKey(Member, on_delete=models.CASCADE)
#     Nurse_Id = models.ForeignKey(Nurse, on_delete=models.CASCADE)
#     Doctor_Id = models.ForeignKey(Doctor, on_delete=models.CASCADE)
#     Date = models.DateField()
#     Frequency = models.PositiveIntegerField()
#     Completed = models.BooleanField(default=False)
#
#     def __str__(self):
#         return f"Special Checkup Schedule for {self.Special_Checkup_Id}"
     

    

    
