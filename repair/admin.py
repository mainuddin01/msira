from django.contrib import admin

from .models import Phone, ProblemType, RepairCharge, Repairables

# Register your models here.
admin.site.register(Phone)
admin.site.register(ProblemType)
admin.site.register(RepairCharge)
admin.site.register(Repairables)
