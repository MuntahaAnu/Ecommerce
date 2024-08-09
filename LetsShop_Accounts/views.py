from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
 
def LOGIN(request):
    if request.method =='POST':
        UserName=request.POST.get('username')
        Pass=request.POST.get('password')
        if len(Pass) == 0:
            messages.warning(request, "No Password Found.")
            return redirect('login')

        user = authenticate(username= UserName, password=Pass)
        if user:
            login(request, user)
            return redirect('home')
    return render(request,'Accounts/login.html')

def REG(request):
    if request.method =='POST':
        First_name=request.POST.get('first')
        Last_name=request.POST.get('last')
        UserName=request.POST.get('name')
        Email=request.POST.get('email')
        Pass=request.POST.get('pass')
        Pass1=request.POST.get('pass1')
        if UserName is not None:
            for i in UserName:
                if i in ['.','@','/','*','$']:
                    messages.warning(request, "Your Username has special character, please remove them.")
                    return redirect('reg')

            if User.objects.filter(username=UserName).exists():
                messages.warning(request, "Your Username already taken! Try New.")
            elif User.objects.filter(email=Email).exists():
                messages.warning(request, "Your Email already taken! Try New.")
            else:
                if Pass == Pass1:
                   user = User.objects.create(first_name=First_name,last_name=Last_name,username=UserName,email=Email,password=Pass)
                   user.set_password(Pass)
                   user.save()
                else:
                    messages.warning(request, "Your Given Password Not Matched.")

    return render(request,'Accounts/registration.html')

def LOGOUT(request):
    logout(request)
    messages.warning(request,"You are logged Out")
    return redirect('login')