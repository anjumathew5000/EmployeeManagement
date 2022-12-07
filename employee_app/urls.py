
from django.urls import path
from . import views
from .views import Addemployee,Addsalary,EmployeeList,DeleteEmployee,EmployeeDetailView,EditEmployee




urlpatterns = [
    path('login',views.login,name="login"),
    path('add_employee',Addemployee.as_view(), name = 'add_employee'),
    path('add_salary/<int:emp_id>', Addsalary.as_view(), name = 'add_salary'),
    path('add_salary', Addsalary.as_view(), name = 'add_salary'),
    path('view_employee',EmployeeList.as_view(),name='view_employee') ,
    path('edit_employee/<int:pk>',EditEmployee.as_view(),name='edit_employee'),
    path('delete_employee/<int:pk>',DeleteEmployee.as_view(),name='delete_employee'),
    path('detail_view_employee/<int:pk>',EmployeeDetailView.as_view(),name='detail_view_employee')
]
