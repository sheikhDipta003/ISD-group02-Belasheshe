from django.db import models
from viewflow.fields import CompositeKey
# from healthcare.models import ResidentRoomAsgn, Doctor, Nurse, MedCond
# from .member import Member
from nurse.models import Nurse
#from doctors.models import Doctor
class Member(models.Model):
    Member_ID = models.IntegerField(primary_key=True, max_length=10)
    # Room_no = models.ForeignKey(ResidentRoomAsgn, on_delete=models.CASCADE)
    Room_no = models.IntegerField()
    Name = models.CharField(max_length=100)
    Address = models.TextField()
    Email = models.EmailField()
    Phone = models.CharField(max_length=15)
    DOB = models.DateField()
    Religion = models.CharField(max_length=50)
    Account_no = models.CharField(max_length=20)

    def __str__(self):
        return self.Name


# Create a model named ResidentMedCond
class ResidentMedCond(models.Model):
    id = CompositeKey(columns=['Member_ID', 'Cond_ID'])
    Member_ID = models.ForeignKey(Member, on_delete=models.CASCADE)
    # Cond_ID = models.ForeignKey(MedCond, on_delete=models.CASCADE)
    Cond_ID = models.IntegerField()

    def __str__(self):
        return f"Medical Condition for {self.Member_ID}"

class MedCond(models.Model):
    Cond_ID=models.AutoField(primary_key=True)
    Name=models.CharField(max_length=50)
    Advice=models.CharField(max_length=150)
    Guideline=models.CharField(max_length=150)
    
# Create a model named MemberAppoint
class MemberAppoint(models.Model):
    App_ID = models.AutoField(primary_key=True)
    Member_ID = models.ForeignKey(Member, on_delete=models.CASCADE)
    # Doctor_ID = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    # Nurse_ID = models.ForeignKey(Nurse, on_delete=models.CASCADE)
    Doctor_ID = models.IntegerField()
    Nurse_ID = models.IntegerField()
    Date = models.DateField()
    Time = models.TimeField()

    def __str__(self):
        return f"Appointment {self.App_ID} for {self.Member_ID}"
<<<<<<< HEAD

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
=======
      
class Medicine(models.Model):
    Medicine_id=models.AutoField(primary_key=True)
    Name=models.CharField(max_length=20)
    Mg=models.IntegerField()
    Company=models.CharField(max_length=50)
    Available=models.IntegerField()

    def __str__(self):
        return f"Checkup {self.Medicine_id}"
    
class MedicineChart(models.Model):
    Chart_id=models.AutoField(primary_key=True)
    Member_id=models.ForeignKey(Member, on_delete=models.CASCADE)
    Date=models.DateField()

    def __str__(self):
        return f"Checkup {self.Chart_id}"
    
class Dosage(models.Model):
    id = CompositeKey(columns=['Chart_id', 'Medicine_id'])
    Chart_id=models.ForeignKey(MedicineChart, on_delete=models.CASCADE)
    Medicine_id=models.ForeignKey(Medicine, on_delete=models.CASCADE)
    #Duration_from=models.DateField()
    #Duration_to=models.DateField()
    #Amount=models.CharField(max_length=20)
    #Frequency=models.CharField(max_length=50)
    Time=models.CharField(max_length=50)
    Quantity=models.CharField(max_length=20)
>>>>>>> c094c3332c935f2ecdb6297fe98d08c0a76d3af2
