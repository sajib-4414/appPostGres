from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.decorators.csrf import csrf_protect
from .models import User

# Create your views here.
def get_index_page(request):
    print("index method")
    return render(request,'index.html')
def get_about_page(request):
    return render(request,'about.html')

@csrf_protect
def login(request):
    print("login method")
    if (request.method == 'POST'):
        # getting post parameters
        email = request.POST.get("email");
        password = request.POST.get("pwd");
        user = User.objects.filter(email=email).filter(password=password)
        if user:#that means we got a valid user
            request.session['name'] = user[0].name
            request.session['email'] = user[0].email
            request.session['phoneno'] = user[0].phone_number
            print(user[0].name)
            return get_index_page(request)
        else:
            messages.error(request, 'email or password error')
            return render(request, 'login.html');
    return render(request, 'login.html');
def logout(request):
    session_keys = list(request.session.keys())
    for key in session_keys:
        del request.session[key]
    return redirect( 'index');

@csrf_protect
def register_user(request):
    if(request.method == 'GET'):
        return render(request, 'register.html');
    else:#request is post
        #getting post parameters
        name = request.POST.get("name");
        email = request.POST.get("email");
        phoneno = request.POST.get("phoneno");
        password = request.POST.get("pwd");
        checkUser = User.objects.filter(email=email)
        if checkUser:#that means user exists
            messages.error(request, 'user with this email already exists')
            return render(request, 'register.html');
        else:
            user = User()
            user.name = name
            user.email = email
            user.password = password
            user.phone_number = phoneno
            user.save();
            request.session['name'] = name
            request.session['email'] = name
            request.session['phoneno'] = phoneno
            return render(request,'index');
