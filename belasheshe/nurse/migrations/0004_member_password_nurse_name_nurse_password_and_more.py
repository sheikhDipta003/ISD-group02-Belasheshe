# Generated by Django 4.2.4 on 2023-09-03 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nurse', '0003_medicine_member_specialcheckupschedule_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='Password',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='nurse',
            name='Name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='nurse',
            name='Password',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='currentcond',
            name='Risk_rate',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='member',
            name='Member_ID',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
