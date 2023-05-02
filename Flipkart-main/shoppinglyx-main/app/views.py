from django.shortcuts import render,HttpResponse,redirect
from .models import product
from django.contrib.auth.models import User 
from django.contrib import messages 
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required 

@login_required(login_url='login')
def home(request):
    
 return render(request, 'app/home.html')

def product_detail(request):
 return render(request, 'app/productdetail.html')

def add_to_cart(request):
 return render(request, 'app/addtocart.html')

def buy_now(request):
 return render(request, 'app/buynow.html')

def profile(request):
 return render(request, 'app/profile.html')

def address(request):
 return render(request, 'app/address.html')

def orders(request):
 return render(request, 'app/orders.html')

def change_password(request):
 return render(request, 'app/changepassword.html')

def mobile(request):
 return render(request, 'app/mobile.html')

def login(request):
    if request.method == 'POST':
        name =  request.POST['name']
        pass1 = request.POST['pass1']        
        user=authenticate(username = name, password = pass1)
        if user is not None:
            # login(request,user)
            auth_login(request, user)
            messages.success(request,"succesfully logedin")
            return redirect('/')
        else:
             messages.error(request,"error in login ")
             return HttpResponse("<h1>Error in password and uername</h1>")
    
    return render(request, 'app/login.html')

def customerregistration(request):
    if request.method =='POST':
       name = request.POST['name']  
       email = request.POST['email'] 
       pass1 = request.POST['pass1'] 
       pass2 = request.POST['pass2']   
    
       if pass1 != pass2:
           return HttpResponse("errroorrr 404")
       else:
            # details = product(name = name,email = email,pass1 = pass1,pass2 = pass2)
            myuser = User.objects.create_user(name,email,pass1)
            myuser.first_name= name
            myuser.save() 
            messages.success(request, " Your iCoder has been successfully created") 
            return redirect('/login/')
        
    return render(request, 'app/customerregistration.html')

def checkout(request):
 return render(request, 'app/checkout.html')


   
def hlogout(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return redirect('/')
