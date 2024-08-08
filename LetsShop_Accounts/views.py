from django.shortcuts import render

# Create your views here.
def LOGIN(request):
    return render(request,'Accounts/login.html')

def REG(request):
    return render(request,'Accounts/registration.html')