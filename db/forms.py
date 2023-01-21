from django import forms
from django.db.models import fields
from .models import *


class emp_form(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ('emp_name', 'emp_id', 'emp_add', 'emp_ad_img')    