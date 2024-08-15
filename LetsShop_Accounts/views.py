from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
import uuid
from django.conf import settings
from .models import *
from django.core.mail import send_mail
def LOGIN(request):
    if request.method =='POST':
        UserName=request.POST.get('username')
        Pass=request.POST.get('password')
        if len(Pass) == 0:
            messages.warning(request, "No Password Found.")
            return redirect('login')

        user = authenticate(username= UserName, password=Pass)
        if user:
            prof = Profile.objects.get(user = user)
            if prof.is_verified == True:
               login(request, user)
               return redirect('home')
        else:
            return redirect('error')
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
                   user = User.objects.create_user(first_name=First_name,last_name=Last_name,username=UserName,email=Email,password=Pass)
                   user.set_password(Pass)
                   auth_token = str(uuid.uuid4())
                   pro_obj = Profile.objects.create(user = user, auth_token = auth_token)
                   pro_obj.save()
                   send_mail_registration(Email, auth_token)
                   return redirect('success')

                   return redirect('login')
                else:
                    messages.warning(request, "Your Given Password Not Matched.")

    return render(request,'Accounts/registration.html')

def LOGOUT(request):
    logout(request)
    messages.warning(request,"You are logged Out")
    return redirect('login')

def RESET_PASS(request):
     if request.method =='POST':
        email=request.POST.get('email')
        Pass=request.POST.get('password')
        Pass1=request.POST.get('password1')

        if User.objects.get(email = email).exists():
            messages.warning(request, "Your User Found.")
            return render('login')

     return render(request,'Accounts/reset_pass.html')

def success(request):
     
     return render(request,'Accounts/success.html')

def token_send(request):
     
     return render(request,'Accounts/token_send.html')

def error(request):
     
     return render(request,'Accounts/error.html')

def send_mail_registration(Email, auth_token):
    subject = 'Your Account Authentication Link'
    message = f'hi, please click the link to verify your account http://127.0.0.1:8000/accounts/verify/{auth_token}'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [Email]
    send_mail(subject, message, email_from, recipient_list)

def verify(request, auth_token):
    profile_obj= Profile.objects.filter(auth_token=auth_token).first()
    profile_obj.is_verified= True
    profile_obj.save()
    messages.success(request,'Congratulation Account Verify its done')
    return redirect('login')