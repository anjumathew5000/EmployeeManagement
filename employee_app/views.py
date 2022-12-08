from django.shortcuts import render,redirect
from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model
from django.views.generic import DetailView,TemplateView
from .models import Employee,Account,Salary
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
        password = request.POST['password']
        print(email,password)
        user = authenticate(email=email, password=password)
        print(user)
       
        if user is not None:
            auth_login(request,user)
            return redirect('home')
        else:
            context={'message':'incorrect email or password'}
            return render(request,'login.html',context)
    else:
        return render(request,'login.html')


def signup(request):
    if request.method == 'POST':
        email    = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        print(email,password,confirm_password)
        if password != confirm_password:
            context={"message":"password did't match"}
            return render(request,'signup.html',context)
        
        user = Account.objects.filter(email=email).first()
      
        if user is not None:
            context={"message":"user already exists"}
            return render(request,'signup.html',context)
      
        obj, created = Account.objects.get_or_create(
        email=email,password=password)
        obj.set_password(password)
        obj.save()

        # context={"message":"user created successfully"}
        return render(request,'login.html')
    
    else:
        return render(request,'signup.html')




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

   def get_context_data(self, **kwargs):
        context = super(EmployeeDetailView, self).get_context_data(**kwargs)
        context['salary'] = Salary.objects.get(employee=context['object']).salary
        return context

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

