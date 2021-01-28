from django.shortcuts import render,redirect
from django.views.generic import TemplateView  
from django.http import HttpResponseRedirect  
from django.contrib import auth  
from django.template.context_processors import csrf 
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from movieupdate.models import Movie
from django.contrib import messages
from django.core.mail import send_mail

# Create your views here.

def login_view(request):    
    c = {}    
    c.update(csrf(request))    
    return render(request, 'login.html', c) 

def auth_view(request):   
    username = request.POST.get('username', '')   
    password = request.POST.get('password', '')   
    user = auth.authenticate(username=username, password=password)
    if username == 'prince' and password == '96449644':#for superuser
        auth.login(request,user)
        return HttpResponseRedirect('/movieupdate/addmovie/')
    if user is not None:    
        auth.login(request, user)  
        return HttpResponseRedirect('/accounts/home/')   
    else:    
        msg = "Invalid Username or Password!"
        return render(request,'login.html',{'msg':msg})

#@login_required('/accounts/login/')
def home_view(request):  
    if request.user.is_authenticated:
        movies=Movie.objects.all()
        if not movies is None:
            return render(request,'home.html',{'movies':movies}) 
    else:
        return redirect('/accounts/login/')

def logout_view(request):
    auth.logout(request)
    return redirect('/accounts/login/')

def forgotpass(request):
    c = {} 
    c.update(csrf(request)) 
    return render(request,'accounts/change_password/done/')

def signup_view(request):
    if request.method=='POST':
        username=request.POST.get('username','')
        password1=request.POST.get('password1','')
        password2=request.POST.get('password2','')
        email=request.POST.get('email','')
        if password1 == password2 and password1 is not None:
            details=User.objects.create_user(username=username,password=password1,email=email)
            details.save()
            user = auth.authenticate(username=username, password=password1)
            auth.login(request, user)   
            return render(request,'login.html') 
        else:
            pwdmsg="RE-ENTER PASSWORD MUST BE SAME AS PASSWORD!!!"
            return render(request,"register.html",{"pwdmsg": pwdmsg})
    else:
        c={}
        c.update(csrf(request))
        return render(request,"register.html")