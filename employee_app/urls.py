
from django.urls import path
from . import views
from .views import Addemployee,Addsalary,EmployeeList,DeleteEmployee,EmployeeDetailView,EditEmployee,HomeView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LogoutView



urlpatterns = [
    path('login',views.login,name="login"),
    path('home',HomeView.as_view(),name="home"),
    path('add_employee',login_required(Addemployee.as_view()), name = 'add_employee'),
    path('add_salary/<int:emp_id>', login_required(Addsalary.as_view()), name = 'add_salary'),
    path('add_salary',login_required(Addsalary.as_view()), name = 'add_salary'),
    path('view_employee',login_required(EmployeeList.as_view()),name='view_employee') ,
    path('edit_employee/<int:pk>',login_required(EditEmployee.as_view()),name='edit_employee'),
    path('delete_employee/<int:pk>',login_required(DeleteEmployee.as_view()),name='delete_employee'),
    path('detail_view_employee/<int:pk>',login_required(EmployeeDetailView.as_view()),name='detail_view_employee'),
    path("logout/", LogoutView.as_view(), name="logout"),
]
