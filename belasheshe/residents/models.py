from django.db import models
# from viewflow.fields import CompositeKey
# from healthcare.models import ResidentRoomAsgn, Doctor, Nurse, MedCond
# from .member import Member
from nurse.models import Nurse,Member
from doctors.models import Doctor

#     def __str__(self):
#         return self.Name

class MedCond(models.Model):
    Cond_ID=models.AutoField(primary_key=True)
    Name=models.CharField(max_length=50)
    Advice=models.CharField(max_length=150)
    Guideline=models.CharField(max_length=150)
# Create a model named ResidentMedCond
class ResidentMedCond(models.Model):
    id = CompositeKey(columns=['Member_ID', 'Cond_ID'])
    Member_ID = models.ForeignKey(Member, on_delete=models.CASCADE)
    Cond_ID = models.ForeignKey(MedCond, on_delete=models.CASCADE)
    # Cond_ID = models.IntegerField()



    
# Create a model named MemberAppoint
class MemberAppoint(models.Model):
    App_ID = models.AutoField(primary_key=True)
    Member_ID = models.ForeignKey(Member, on_delete=models.CASCADE)
    Doctor_ID = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    Nurse_ID = models.ForeignKey(Nurse, on_delete=models.CASCADE)
    # Doctor_ID = models.IntegerField()
    # Nurse_ID = models.IntegerField()
    Date = models.DateField()
    Time = models.TimeField()



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
     

    def __str__(self):
        return f"Medicine {self.Medicine_id} {self.Name}"
    

    def __str__(self):
        return f"Medicine chart {self.Chart_id} for {self.Member_id}"
    
class Dosage(models.Model):
    id = CompositeKey(columns=['Chart_id', 'Medicine_id'])
    Medicine_id=models.ForeignKey(Medicine, on_delete=models.CASCADE)
    Chart_id=models.ForeignKey(MedicineChart, on_delete=models.CASCADE)
    Time=models.CharField(max_length=50)
    Quantity=models.CharField(max_length=20)

class CurrentCond(models.Model):
    Member_id=models.ForeignKey(Member, on_delete=models.CASCADE)
    Risk_rate=models.IntegerField(max_length=3)
    def __str__(self):
        return f"{self.Member_id} {self.Risk_rate}"
