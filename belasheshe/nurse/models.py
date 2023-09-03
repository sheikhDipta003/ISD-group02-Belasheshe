from django.db import models
from doctors.models import Doctor
# from residents.models import Member
# Create your models here.
class Nurse(models.Model):
    Nurse_Id = models.AutoField(primary_key=True)
    Qualifications = models.CharField(max_length=50)
    Shift = models.CharField(max_length=20)
    Name=models.CharField(max_length=50, default='Unknown')
    

    def __str__(self):
        return f"Checkup {self.Nurse_Id} Qualifications {self.Qualifications} Shift {self.Shift}"

class Member(models.Model):
    Member_ID = models.AutoField(primary_key=True)
    # Room_no = models.ForeignKey(ResidentRoomAsgn, on_delete=models.CASCADE)
    Room_no = models.IntegerField()
    Name = models.CharField(max_length=100)
    Address = models.TextField()
    Email = models.EmailField()
    Phone = models.CharField(max_length=15)
    DOB = models.DateField()
    Religion = models.CharField(max_length=50)
    Account_no = models.CharField(max_length=20)
    Assigned_nurse=models.ForeignKey(Nurse, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.Name} {self.Member_ID}"


class CheckupItem(models.Model):
    Checkup_Id = models.AutoField(primary_key=True)
    Blood_Pressure = models.CharField(max_length=20)
    Sugar = models.DecimalField(max_digits=5, decimal_places=2)
    Heartrate = models.IntegerField()

    def __str__(self):
        return f"Checkup {self.Checkup_Id}"

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
