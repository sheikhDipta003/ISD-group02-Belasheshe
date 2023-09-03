from django.contrib import admin
from .models import MedCond, CheckupItem
# Register your models here.

admin.site.register(MedCond)
admin.site.register(CheckupItem)