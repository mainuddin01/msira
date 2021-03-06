from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

User = get_user_model()

# Create your models here.
class Brand(models.Model):
    name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.name

class Phone(models.Model):
    name = models.CharField(max_length=50, unique=True)
    brand = models.ForeignKey('Brand', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='phone_images')

    def get_absolute_url(self):
        return reverse('repair:phone_detail', kwargs={'pk':self.pk})

    def __str__(self):
        return self.name


class Problem(models.Model):
    # phone = models.ForeignKey('Phone', on_delete=models.CASCADE)
    name = models.CharField(max_length=50, unique=True)
    # name = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)
    # repair_charge = models.DecimalField(max_digits=10, decimal_places=2)

    def get_absolute_url(self):
        # return reverse('repair:problem_type_detail', kwargs={'pk':self.pk})
        return reverse('repair:dashboard_problem_type_list')

    def __str__(self):
        return self.name


class PhoneProblem(models.Model):
    phone = models.ForeignKey('Phone', on_delete=models.CASCADE)
    problem = models.ForeignKey('Problem', on_delete=models.CASCADE)
    charge = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.phone.name} - {self.problem.name}"


class Repairables(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    phone_problems = models.ManyToManyField('PhoneProblem')
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_at = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.id


class Color(models.Model):
    color = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.color
