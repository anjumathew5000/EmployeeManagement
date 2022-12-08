from django.forms import fields  
from .models import Employee ,Salary 
from django import forms  
  
class EmployeeForm(forms.ModelForm):  
  
    class Meta:  
        # To specify the model to be used to create form  
        model = Employee  
        # It includes all the fields of model  
        fields = '__all__'  

class SalaryForm(forms.ModelForm):  
  
    class Meta:  
        # To specify the model to be used to create form  
        model = Salary  
        # It includes all the fields of model  
        fields = ['salary'] 

# class ValidateEmployeeForm(forms.ModelForm):
#     email = forms.EmailField()
#     first_name = forms.CharField(validators=[validators.MinLengthValidator(2, message="Please enter the valid name")])
#     last_name = forms.CharField(validators=[validators.MinLengthValidator(2, message="Please enter the valid name")])
#     employee_code = forms.CharField(validators=[validators.MinLengthValidator(, message="Please enter the valid name")])
#      = forms.CharField(validators=[
#                                     validators.MinLengthValidator(2, message='Please enter the valid message'),
#                                     validators.MaxLengthValidator(1000)
#                                 ])

#     class Meta:
#         model = Employee  
#         fields = ("email", "first_name", "last_name","phone")