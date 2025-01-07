from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from .models import *
from django.shortcuts import render, redirect, get_object_or_404
from datetime import datetime



def index(request):
    return render(request, 'index.html')

def registration(request):
    error = ""
    if request.method == "POST":
        try:
            fn = request.POST.get('Firstname')
            ln = request.POST.get('Lastname')
            ei = request.POST.get('empid')
            em = request.POST.get('email')
            pwd = request.POST.get('pwd')
            
            user = User.objects.create_user(
                first_name=fn,
                last_name=ln,
                username=em,
                email=em,
                password=pwd
            )

            EmployeeDetail.objects.create(user=user, empid=ei)
            EmployeeExperience.objects.create(user=user)
            EmployeeEducation.objects.create(user=user)
            error = "No"  

        except Exception as e:
            print(f"Error: {e}")  
            error = "Yes"  

    return render(request, 'registration.html', locals())

def emp_login(request):
    error = ""
    if request.method == 'POST':
        u = request.POST.get('emailid')  # Get email from form
        p = request.POST.get('password')  # Get password from form
        user = authenticate(username=u, password=p)  # Authenticate user
        
        if user:  # If user is valid
            login(request, user)  # Log the user in
            return redirect('emp_home')  # Redirect to emp_home page
        else:
            error = "Yes"  # Login failed

    return render(request, 'emp_login.html', {'error': error})  # Pass error to template


def emp_home(request):
    if not request.user.is_authenticated:
        return redirect('emp_login')
    return render(request, 'emp_home.html', locals())


def Logout(request):
    logout(request)
    return redirect('index')


def profile(request):
    if not request.user.is_authenticated:
        return redirect('emp_login')
    
    error = ""
    try:
        user = request.user
        employee = EmployeeDetail.objects.get(user=user)
    except EmployeeDetail.DoesNotExist:
        employee = None
        error = "Employee details not found. Please contact support."
    
    if request.method == "POST" and employee:  
        fn = request.POST.get('Firstname')
        ln = request.POST.get('Lastname')
        ei = request.POST.get('empid')
        de = request.POST.get('department')
        dn = request.POST.get('designation')
        ct = request.POST.get('contact')
        jd = request.POST.get('jdate')  
        gd = request.POST.get('gender')
        
        employee.user.first_name = fn
        employee.user.last_name = ln
        employee.empid = ei
        employee.empdept = de
        employee.designation = dn
        employee.contact = ct
        employee.gender = gd
        
        if jd:  
            employee.joiningdate = jd
        
        try:
            employee.save()
            employee.user.save()
            error = "No"  
        except Exception as e:
            print(f"Error saving employee details: {e}")
            error = "Yes"
    
    return render(request, 'profile.html', {'error': error, 'employee': employee})

def admin_login(request):
    if not request.user.is_authenticated:
        return redirect('emp_login')
    return render(request, 'admin_login.html', locals())

def myexperience(request):
    if not request.user.is_authenticated:
        return redirect('emp_login')
    
    user = request.user
    experience = EmployeeExperience.objects.get(user=user)
   
    return render(request, 'myexperience.html',locals())


def edit_myexperience(request):
    if not request.user.is_authenticated:
        return redirect('emp_login')
    
    error = ""
    try:
        user = request.user
        experience = EmployeeExperience.objects.get(user=user)
    except EmployeeExperience.DoesNotExist:
        experience = None
        error = "Employee details not found. Please contact support."
    
    if request.method == "POST" and experience:  
        company1name = request.POST.get('company1name')
        company1desig = request.POST.get('company1desig')
        company1salary = request.POST.get('company1salary')
        company1duration = request.POST.get('company1duration')
        
        company2name = request.POST.get('company2name')
        company2desig = request.POST.get('company2desig')
        company2salary = request.POST.get('company2salary')
        company2duration = request.POST.get('company2duration')
        
        company3name = request.POST.get('company3name')
        company3desig = request.POST.get('company3desig')
        company3salary = request.POST.get('company3salary')
        company3duration = request.POST.get('company3duration')
        
        experience.company1name= company1name
        experience.company1desig = company1desig
        experience.company1salary = company1salary
        experience.company1duration = company1duration
        
        experience.company2name= company2name
        experience.company2desig = company2desig
        experience.company2salary = company2salary
        experience.company2duration = company2duration
        
        experience.company3name= company3name
        experience.company3desig = company3desig
        experience.company3salary = company3salary
        experience.company3duration = company3duration
        
        try:
            experience.save()
            error = "No"  
        except Exception as e:
            print(f"Error saving experience details: {e}")
            error = "Yes"
    
    return render(request, 'edit_myexperience.html', locals())


def my_education(request):
    if not request.user.is_authenticated:
        return redirect('emp_login')
    
    user = request.user
    education = EmployeeEducation.objects.get(user=user)
   
    return render(request, 'my_education.html',locals())


def edit_myeducation(request):
    if not request.user.is_authenticated:
        return redirect('emp_login')
    
    error = ""
    try:
        user = request.user
        education = EmployeeEducation.objects.get(user=user)
    except EmployeeExperience.DoesNotExist:
        educartion = None
        error = "Employee details not found. Please contact support."
    
    if request.method == "POST" and education:  
        company1name = request.POST.get('company1name')
        company1desig = request.POST.get('company1desig')
        company1salary = request.POST.get('company1salary')
        company1duration = request.POST.get('company1duration')
        
        company2name = request.POST.get('company2name')
        company2desig = request.POST.get('company2desig')
        company2salary = request.POST.get('company2salary')
        company2duration = request.POST.get('company2duration')
        
        company3name = request.POST.get('company3name')
        company3desig = request.POST.get('company3desig')
        company3salary = request.POST.get('company3salary')
        company3duration = request.POST.get('company3duration')
        
        education.company1name= company1name
        education.company1desig = company1desig
        education.company1salary = company1salary
        education.company1duration = company1duration
        
        education.company2name= company2name
        education.company2desig = company2desig
        education.company2salary = company2salary
        education.company2duration = company2duration
        
        education.company3name= company3name
        education.company3desig = company3desig
        education.company3salary = company3salary
        education.company3duration = company3duration
        
        try:
            education.save()
            error = "No"  
        except Exception as e:
            print(f"Error saving experience details: {e}")
            error = "Yes"
    
    return render(request, 'edit_myeducation.html', locals())


def change_password(request):
    if not request.user.is_authenticated:
        return redirect('emp_login')
    
    error = ""
    user = request.user
       
    if request.method == "POST":  
        c = request.POST['currentpassword']
        n = request.POST['newpassword']
        try:
            if user.check_password(c):
                user.set_password(n)
                user.save()
                error = "No"  
            else:
                error = "not"
        except:
            error = "Yes"
    return render(request,'change_password.html',locals())

def admin_login(request):
    error = None 
    if request.method == 'POST':
        u = request.POST.get('username')  
        p = request.POST.get('pwd')  
        user = authenticate(username=u, password=p) 

        if user:
            if user.is_staff:  
                login(request, user)  
                return redirect('admin_home')  
            else:
                error = "You do not have admin privileges." 
        else:
            error = "Invalid username or password."  

        print(f"Error: {error}")  

    return render(request, 'admin_login.html', {'error': error})


def admin_home(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    return render(request, 'admin_home.html')

def change_passwordadmin(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    
    error = ""
    user = request.user
       
    if request.method == "POST":  
        c = request.POST['currentpassword']
        n = request.POST['newpassword']
        try:
            if user.check_password(c):
                user.set_password(n)
                user.save()
                error = "No"  
            else:
                error = "not"
        except:
            error = "Yes"
    return render(request,'change_passwordadmin.html',locals())


def all_employee(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    
    employee = EmployeeDetail.objects.all()
    return render(request, 'all_employee.html', locals())

def edit_employee(request, id):
    employee = get_object_or_404(EmployeeDetail, id=id)
    if request.method == 'POST':
        employee.empid = request.POST.get('empid')
        employee.empdept = request.POST.get('empdept')
        employee.designation = request.POST.get('designation')
        employee.contact = request.POST.get('contact')
        employee.gender = request.POST.get('gender')
        
        # Convert the joiningdate to the proper format
        joiningdate = request.POST.get('joiningdate')
        if joiningdate:
            employee.joiningdate = datetime.strptime(joiningdate, "%Y-%m-%d").date()

        employee.save()
        return redirect('all_employee')
    return render(request, 'edit_employee.html', {'employee': employee})


def delete_employee(request, id):
    employee = get_object_or_404(EmployeeDetail, id=id)
    if request.method == 'POST':
        employee.delete()
        return redirect('all_employee')
    return render(request, 'delete_employee.html', {'employee': employee})