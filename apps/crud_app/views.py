from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect
from .models import User

# Create your views here.
def get_index_page(request):
    return render(request,'index.html');
def get_about_page(request):
    return render(request,'about.html');

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
        user = User()
        user.name = name
        user.email = email
        user.password = password
        user.phone_number = phoneno
        user.save();
        request.session['name'] = name
        request.session['email'] = name
        request.session['phoneno'] = phoneno
        return redirect('/app');
