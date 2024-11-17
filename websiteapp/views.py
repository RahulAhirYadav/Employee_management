from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *

# function based view

def home(request):
    return render(request,'index.html')

def company(request):
    company_data = Company.objects.all().first()
    context={'company_data':company_data}
    return render(request,'company.html',context)

def service(request):
    department_data = Department.objects.all()
    context={'department_data':department_data}
    return render(request,'service.html',context)

def Emp_attendence(request):
    dept_list = Department.objects.all()
    data = request.GET.get('dlist')
    employee_list = Employee.objects.all()
    if data:
        employee_list = Employee.objects.filter(department=data)
        context={'employee_list':employee_list,'dept_list':dept_list}
    return render(request,'Employee_list.html',context)

def contact(request):
    if request.method=="POST":
        name=request.POST['name']
        phone=request.POST['phone']
        email=request.POST['email']
        message=request.POST['message']
        data=Contact(name=name,phone=phone,email=email,message=message)
        data.save()
        return redirect('home')
    else:
        return render(request,'contact.html')

#my changes

def attendance_form(request):
    departments = Department.objects.all()
    employees = None  # Initialize employees variable here
    selected_department = None
    selected_status = None

    if request.method == 'GET':
        department_id = request.GET.get('department_id')
        status = request.GET.get('status')
        
        if department_id:
            selected_department = Department.objects.get(pk=department_id)
            employees = Employee.objects.filter(department_id=department_id)
            
            if status:
                employees = employees.filter(status=status)
                selected_status = status

    elif request.method == 'POST':
        department_id = request.POST.get('department_id')
        status = request.POST.get('status')
        attendance_date = request.POST.get('date')
        
        if department_id:
            selected_department = Department.objects.get(pk=department_id)
            employees = Employee.objects.filter(department_id=department_id)
            
            if status:
                employees = employees.filter(status=status)
                selected_status = status
                
            for employee in employees:
                status_key = f'employee_{employee.id}_status'
                attendance_status = request.POST.get(status_key)
                EmpAttendence.objects.create(
                    employee=employee,
                    department_name=employee.department,
                    date=attendance_date,
                    present_status=attendance_status
                )
        msg="Your attendance has been successfully saved"
        return redirect('attendance_form',{'msg':msg})

    return render(request, 'att.html', {
        'departments': departments,
        'employees': employees,
        'selected_department': selected_department,
        'selected_status': selected_status,
    })

def view_attendance(request):
    # Get all attendance records initially
    attendance_records = EmpAttendence.objects.all()

    # Get distinct department IDs for filtering options
    department_ids = EmpAttendence.objects.values_list('department_name_id', flat=True).distinct()

    # Get all departments
    departments = Department.objects.filter(pk__in=department_ids)

    # Apply filters if provided
    department_id = request.GET.get('department_id')
    date = request.GET.get('date')
    present_status = request.GET.get('present_status')

    if department_id:
        attendance_records = attendance_records.filter(department_name_id=department_id)

    if date:
        attendance_records = attendance_records.filter(date=date)

    if present_status:
        attendance_records = attendance_records.filter(present_status=present_status)

    context = {
        'attendance_records': attendance_records,
        'departments': departments,  # Pass department options to the template
        'selected_department_id': department_id,  # Pass selected department ID for retaining selection
        'selected_date': date,  # Pass selected date for retaining selection
        'selected_present_status': present_status  # Pass selected status for retaining selection
    }
    return render(request, 'view_attendance.html', context)


####if user login the show take attandance and show attandance

from django.contrib.auth import authenticate, login,logout

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
def Login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
    
                return redirect('home')  # Redirect to the home page after login
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})



def Register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Login')  # Redirect to login page after successful registration
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('home')