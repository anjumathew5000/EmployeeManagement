from django.shortcuts import render,redirect
from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model
from django.views.generic import DetailView,TemplateView
from .models import Employee,Account
from django.views.generic.edit import UpdateView,CreateView,DeleteView
from django.views.generic.list import ListView
from .forms import EmployeeForm,SalaryForm
from django.http import JsonResponse
from django.contrib.auth.hashers import check_password
from django.contrib.auth import login as auth_login
from django.http import HttpResponseRedirect

# Create your views here.


def login(request):
    if request.method == 'POST':
        email    = request.POST['email']
        user = Account.objects.get(email=email)
        user.backend = 'django.contrib.auth.backends.ModelBackend'
       
        if user is not None:
            auth_login(request, user)
            return redirect('home')
        else:
            context={'message':'email incorrect'}
            return render(request,'login.html',context)
    else:
        return render(request,'login.html')


class HomeView(TemplateView):
    template_name ='home.html'

class Addemployee(CreateView): 
    def get(self, request, *args, **kwargs):
        
        return render(request, 'add_employee.html')
        
    
    def post(self, request, *args, **kwargs):
        try:
            if self.request.method == "POST":
                form =EmployeeForm(self.request.POST)
              
                if form.is_valid():
                    form.save()
                    print("yesssssssssss")
                    emp_code = form.cleaned_data['employee_code']
                    emp_id=Employee.objects.get(employee_code=emp_code).id
                    print(emp_id)
                    d = {"success": True,"emp_id":emp_id}
                    return JsonResponse(d, status=200)
                else:
                    return JsonResponse({"success": False, "errors": form.errors.as_json()}, status=403)
            else:
                return JsonResponse({"success": False}, status=400)
        except Exception as e:
            return JsonResponse({"success": False}, status=400)
    
class Addsalary(CreateView): 
    def get(self, request, *args, **kwargs):
        
        emp_id = self.kwargs['emp_id']
        emp_data =Employee.objects.get(id=emp_id)
        context={'employee':emp_data}
        
        return render(request, 'add_salary.html',context)
        
    def post(self, request, *args, **kwargs):
        try:
            if self.request.method == "POST":
                emp_id = self.request.POST['id']
                form =SalaryForm(self.request.POST)
                emp_data = Employee.objects.get(id=emp_id)
                # employee_code = emp_data.employee_code
                # if Salary.objects.filter(employee=emp_data).exists():
                #     print("yes")
                #     d={"success": False,"errors":"This Employee salary is already added !"}
                #     return JsonResponse(d,status=400)
                if form.is_valid():
                    obj = form.save(commit=False)
                    obj.employee= emp_data
                    obj.save()
                    d = {"success": True}
                    return JsonResponse(d,status=200)
                    
                else:
                    return JsonResponse({"success": False, "errors": form.errors.as_json()}, status=403)
            else:
                return JsonResponse({"success": False}, status=400)
        except Exception as e:
            return JsonResponse({"success": False}, status=400)


class EmployeeList(ListView):
    model = Employee
    template_name ='view_employee.html'
    context_object_name = 'employee_list'

class EmployeeDetailView(DetailView):
   model = Employee
   template_name = 'employee_detail.html'

class EditEmployee(UpdateView):
    model = Employee
    fields = [
        "first_name",
        "last_name",
        "role",
        "phone",
        "email"

    ]
 
    template_name = 'edit_employee.html'
    success_url = '/view_employee'


class DeleteEmployee(DeleteView):
    model = Employee
    template_name = 'delete_employee.html'
    success_url = '/view_employee'

