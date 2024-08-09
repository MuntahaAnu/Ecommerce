from django.shortcuts import render
from django.contrib.auth.models import User

 
def LOGIN(request):
    return render(request,'Accounts/login.html')

def REG(request):
    if request.method =='POST':
        First_name=request.POST.get('first')
        Last_name=request.POST.get('last')
        UserName=request.POST.get('name')
        Email=request.POST.get('email')
        Pass=request.POST.get('pass')
        Pass1=request.POST.get('pass1')
        if Pass == Pass1:
           user = User.objects.create(first_name=First_name,last_name=Last_name,username=UserName,email=Email,password=Pass)
           user.set_password(Pass)
           user.save()

    return render(request,'Accounts/registration.html')