from django.shortcuts import render,redirect
from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model
from django.views.generic import DetailView,TemplateView
from .models import Employee
from django.views.generic.edit import UpdateView,CreateView,DeleteView
from django.views.generic.list import ListView
from .forms import EmployeeForm,SalaryForm
from django.http import JsonResponse

# Create your views here.

def login(request):
    if request.method == 'POST':
        email    = request.POST['email']
        password = request.POST['password']
        print(email)
        print(password)
        user = authenticate(username=email, password=password)
        print(user)
        if user is not None:
            
            # A backend authenticated the credentials
            return redirect('add_employee')
        else:
            # No backend authenticated the credentials
            context={'message':'email or password incorrect'}
            return render(request,'login.html',context)
    else:
         return render(request,'login.html')



class Addemployee(CreateView): 
    def get(self, request, *args, **kwargs):
        # checkUser(request)
        print("yessss")
        return render(request, 'add_employee.html')
    
    def post(self, request, *args, **kwargs):
        try:
            if self.request.method == "POST":
                form =EmployeeForm(self.request.POST)
              
                if form.is_valid():
                    form.save()
                    
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
        # checkUser(request)
        emp_id = self.kwargs['emp_id']
        emp_data =Employee.objects.get(id=emp_id)
        context={'employee':emp_data}
        return render(request, 'add_salary.html',context)
        
    def post(self, request, *args, **kwargs):
        try:
            if self.request.method == "POST":
                emp_id = self.request.POST['id']
                form =SalaryForm(self.request.POST)
                if form.is_valid():

                    obj = form.save(commit=False)
                    obj.employee= Employee.objects.get(id=emp_id)
                    obj.save()
                
                    d = {"success": True}
                   
                    return JsonResponse(d, status=200)
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
    # form_class = Employee
    # pk_url_kwarg = 'pk'
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

