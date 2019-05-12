from django.contrib import admin

from .models import Phone, Problem, PhoneProblem, Repairables

# Register your models here.
admin.site.register(Phone)
admin.site.register(Problem)
admin.site.register(PhoneProblem)
admin.site.register(Repairables)
