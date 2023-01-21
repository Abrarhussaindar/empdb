from django.db import models


class Employee(models.Model):
    emp_name = models.CharField(verbose_name='Employee Name', max_length=200, null=True)
    emp_id = models.CharField(verbose_name='Employee ID', max_length=200, null=True)
    emp_add = models.CharField(verbose_name='Employee Address', max_length=800, null=True)
    emp_ad_img = models.ImageField(verbose_name='Employee Adhar Card Image',null=True)

    def __str__(self):
        return self.emp_name