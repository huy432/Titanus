from http.client import responses
from django.shortcuts import render
from django.http import HttpResponse
from .forms import RegistrationForm
from django.http import HttpResponseRedirect 
import django.contrib.auth as auth
from .models import UserProfile
from django.contrib.auth.models import User
import smtplib

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            if UserProfile.objects.get(user=user).isActive == False:
                return render(request, "login/login.html", {"username": username,"error":2})
            auth.login(request, user)
        else:
            return render(request, "login/login.html", {"error":1,"username": username})
    return render(request, "login/login.html", {"username": "","error":0})
def register(request):
    form = RegistrationForm()
    
    context = {
        "error":"",
        "form":form
    }
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            user = User.objects.get(username=request.POST['username'])
            if user:
                userprofile = UserProfile()
                userprofile.user = user
                userprofile.description = "."
                userprofile.isActive = False
                userprofile.save()
                sendVef(user)
            
            
            return HttpResponseRedirect('/')
        else:
            context["error"] = form.error
    return render(request, "register/register.html", context)

def profile(request):
    context = {}
    context["username"] = request.user.username
    context["name"] = request.user.first_name
    if request.user.is_authenticated:
        context["avatar"] = str(UserProfile.objects.get(user=request.user).avatar)
    else:
        context["avatar"] = "0"
    return render(request, "profile/profile.html", context)

def sendVef(user):
    
    sender_add='thongthai1504@gmail.com' 
    receiver_add=user.email
    password='yzuthmbtpgaqmsoq' 
    
    smtp_server=smtplib.SMTP("smtp.gmail.com",587 )
    smtp_server.ehlo() 
    smtp_server.starttls() 
    smtp_server.ehlo() 
    smtp_server.login(sender_add,password) 
    msg_to_be_sent ='''
    Click to verification your account
    http://localhost:8000/account/verification/{}/{}
    Thank you for used my project
    '''.format(user.username,UserProfile.objects.get(user=user)._a)
    
    smtp_server.sendmail(sender_add,receiver_add,msg_to_be_sent)
    smtp_server.quit()

def verificationAccount(request, username, data):
    user = User.objects.get(username=username)
    userProfile = UserProfile.objects.get(user=user)
    if userProfile.isActive:
        return HttpResponseRedirect('/')
    else:
        if userProfile._a == data:
            userProfile.isActive = True
            userProfile.save()
            return render(request, "verification/verification.html")
        else:
            return render(request, "error.html")