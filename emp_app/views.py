from django.http import HttpResponse
from django.shortcuts import render,redirect
from. models import *
from datetime import datetime
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def SignupPage(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')

        if pass1!=pass2:
            return HttpResponse("Your password and confrom password are not Same!!")
        else:

            my_user=CustomUser.objects.create_user(full_name=uname,email=email,password=pass1,confirm_password=pass2)
            my_user.save()
            return redirect('login')
        
    return render (request,'signup.html')



def LoginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('index')
        else:
            return HttpResponse ("Username or Password is incorrect!!!")

    return render (request,'login.html')

@login_required
def index(request):
    return render(request,'index.html')

@login_required
def all_emp(request):
    emps=Employee.objects.all()
    context={
        'emps':emps
    }
    print(context)
    return render(request,'view_all_emp.html',context)

@login_required
def add_emp(request):
    if request.method =='POST':
        first_name=request.POST['first_name']
        Last_name=request.POST['Last_name']
        salary=int(request.POST['salary'])
        bonus=int(request.POST['bonus'])
        phone=int(request.POST['phone'])
        dept=int(request.POST['dept'])
        role=int(request.POST['role'])
        new_emp=Employee(first_name= first_name, Last_name=Last_name,salary=salary,bonus=bonus,phone=phone,dept_id=dept,role_id=role,hire_date=datetime.now())
        new_emp.save()
        return HttpResponse("Employee added suceesfully")
    elif request.method=='GET':
        return render(request,'add_emp.html')    
    else:
        return HttpResponse("An Exception Occured Employee Has Not Been Added")    


@login_required 
def remove_emp(request, emp_id = 0):
     if emp_id:
        try:
            emp_to_be_removed =Employee.objects.get(id=emp_id)
            emp_to_be_removed.delete()
            return HttpResponse("Employee Removed Sucessfully")
           
        except:
             return HttpResponse("Please Enter A valid EMP ID ")
     emps=Employee.objects.all()
     context={

        'emps':emps
    }
     return render(request,'remove_emp.html',context)    
        
@login_required
def filter_emp(request):
    if request.method =='POST':
        name=request.POST['name']
        dept=request.POST['dept']
        role=request.POST['role']
        #emps=Employee.objects.all()
        parameters = Q(Q(first_name__icontains=name) | Q(Last_name__icontains=name))
        emps=Employee.objects.filter(parameters).values()
          
        context ={
            'emps':emps
        }    
        return render(request,'filter_emp.html',context)

    elif request.method =='GET':

        return render(request,'filter_emp.html')
    else:
        return HttpResponse('An Exception Occured')    

def LogoutPage(request):
    logout(request)
    return redirect('login')

            

        

            

            

