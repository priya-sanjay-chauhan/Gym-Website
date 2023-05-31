from django.shortcuts import render,HttpResponse,redirect
from .models import data
from .models import contact_detail
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

# Create your views here.
def first(request):
    alert=''
    if request.method=='POST':
        Name=request.POST.get('Name')
        Email=request.POST.get('Email')
        Phone=request.POST.get('Phone')
        Gender=request.POST.get('Gender')
        DOB=request.POST.get('DOB')
        Address=request.POST.get('Address')
        a=data(Name=Name,Email=Email,Phone=Phone,Gender=Gender,DOB=DOB,Address=Address)
        a.save()
        alert='Data saved'

    return render(request, 'home.html',{'alert':alert})


def handlesignup(request):
    if request.method=='POST':
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password1')
        confirmpassword=request.POST.get('password2')
        # print(username,email,password,confirmpassword)

        if password!=confirmpassword:
            messages.warning(request,"Password is incorrect")
            return redirect('/signup')

        try:
            if User.objects.get(username=username):
                messages.info(request,"Username is taken")
                return redirect('/signup')
        except:
            pass

        try:
            if User.objects.get(email=email):
                messages.info(request,"Email already exists")
                return redirect('/signup')
        except:
            pass


        myuser=User.objects.create_user(username,email,password)
        myuser.save()
        messages.info(request,"Signup successfully. Please login!")
        return redirect('/login')

    return render(request,'signup.html')




def handlelogin(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        pass1=request.POST.get('pass1')
        myuser=authenticate(username=uname,password=pass1)
        if myuser is not None:
            login(request,myuser)
            messages.success(request,"Login Successfully")
            return redirect('/')

        else:
            messages.error(request,"Invalid")
            return redirect('/login')

    return render(request,'login.html')




def handlelogout(request):
    logout(request)
    messages.info(request,"Logout successfully")
    return redirect("/login")
    


def contact(request):
    if request.method=='POST':
        username=request.POST.get('username')
        email=request.POST.get('email')
        description=request.POST.get('description')
        contact_data=contact_detail(Username=username,Email=email,Message=description)
        contact_data.save()

        
        messages.info(request,"Your response has been recorded")
        # return redirect("/contact")

    return render(request, 'contact.html')


def program(request):
    return render(request,"program.html")