from django.contrib import admin
from .models import Account,Employee,Salary

# Register your models here.
admin.site.register(Account)
admin.site.register(Employee)
admin.site.register(Salary)