# Generated by Django 4.2.4 on 2023-09-02 12:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('doctors', '0001_initial'),
        ('nurse', '0002_nurse_delete_healthdata'),
    ]

    operations = [
        migrations.CreateModel(
            name='CheckupItem',
            fields=[
                ('Checkup_Id', models.AutoField(primary_key=True, serialize=False)),
                ('Blood_Pressure', models.CharField(max_length=20)),
                ('Sugar', models.DecimalField(decimal_places=2, max_digits=5)),
                ('Heartrate', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('Member_ID', models.AutoField(primary_key=True, serialize=False)),
                ('Room_no', models.IntegerField()),
                ('Name', models.CharField(max_length=100)),
                ('Address', models.TextField()),
                ('Email', models.EmailField(max_length=254)),
                ('Phone', models.CharField(max_length=15)),
                ('DOB', models.DateField()),
                ('Religion', models.CharField(max_length=50)),
                ('Account_no', models.CharField(max_length=20)),
                ('Assigned_nurse', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nurse.nurse')),
            ],
        ),
        migrations.CreateModel(
            name='SpecialCheckupSchedule',
            fields=[
                ('Special_Checkup_Id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='nurse.checkupitem')),
                ('Date', models.DateField()),
                ('Frequency', models.PositiveIntegerField()),
                ('Completed', models.BooleanField(default=False)),
                ('Doctor_Id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='doctors.doctor')),
                ('Member_Id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nurse.member')),
                ('Nurse_Id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nurse.nurse')),
            ],
        ),
        migrations.CreateModel(
            name='CheckupSchedule',
            fields=[
                ('Checkup_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='nurse.checkupitem')),
                ('Date', models.DateField()),
                ('Completed', models.BooleanField(default=False)),
                ('Doctor_Id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='doctors.doctor')),
                ('Member_Id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nurse.member')),
                ('Nurse_Id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nurse.nurse')),
            ],
        ),
    ]
