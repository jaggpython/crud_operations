from django import forms  
from employee.models import Employee
from django.forms import fields

class EmployeeForm(forms.ModelForm):  
    class Meta:  
        model = Employee  
        fields = "__all__"  