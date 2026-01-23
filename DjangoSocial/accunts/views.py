from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages



# Create your views here.
def register(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        email=request.POST.get('email')
        

        user=User.objects.filter(username=username).exists()
        if user:
            messages.error(request,"username already taken")
            return redirect("login")
        user=User.objects.create_user(
            username=username,email=email,password=password
        )

        user.save()
        messages.info(request,"user created")
        return redirect("login")
    return render(request,"register.html")

def login_page(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')

        user=authenticate(request=request,username=username,password=password)
        print(user)
        if user is not None:
            login(request,user)
            messages.success(request,"login success")
            return redirect("profile")
        else:
            messages.error(request,"invalid user and password")
    return render(request,"login.html")

def logout_page(request):
    logout(request)
    messages.info(request,"Logout Succeccfull")
    return redirect("login")

@login_required(login_url="login")
def reset_pass(request):
    if request.method=="POST":
        username=request.POST['username']
        oldpass=request.POST['oldpassword']
        newpass=request.POST['newpassword']

        user=authenticate(username=username,password=oldpass)

        if user:
            user.set_password(newpass)
            messages.success(request,"Password Chanded Successfulyy!!")
            return redirect("login")
    return render(request,"resetpass.html")


def forgetPass(request):
    if request.method=='POST':
        username=request.POST['username']
        email=request.POST['email']

        user=User.objects.get(username=username,email=email)
        print(user.id)
        if user:
            return redirect("forgetreset",user.id)
        else:
            messages.error(request,"wrong username and email")
            return redirect("forgetPass")
    return render(request,"forgetPass.html")

def resetforget(request,id):
    users=User.objects.get(id=id)
    if request.method=='POST':
        pass1=request.POST['password1']
        pass2=request.POST['password2']
        if users:
            if pass1==pass2:
                users.set_password(pass1)
                users.save()
                return redirect("login")
    
    return render(request,"forgetreset.html")
