from django.contrib import admin

from .models import Phone, ProblemType, RepairProblem, Repairables

# Register your models here.
admin.site.register(Phone)
admin.site.register(ProblemType)
admin.site.register(RepairProblem)
admin.site.register(Repairables)
