from django.shortcuts import render,redirect
from django.http import HttpResponse
from ABCapp.forms import *
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from  django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user,allowed_user,admin_only




@unauthenticated_user
def loginpage(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.warning(request, 'invalid user name or password')
    return render(request, 'login.html')

@unauthenticated_user
def registerpage(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = request.POST.get('username')
            messages.success(request, "Account creating successfully for " + user)
            return redirect('login')
    contxt = {'form': form}
    return render(request,'register.html',contxt)


@login_required(login_url='login')

def home(request):
    return render(request,'dashboard.html')


@login_required(login_url='login')
def logoutpage(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')

def footerpage(request):
    return render(request,'footer.html')

@login_required(login_url='login')
def mainBook(request):
    return render(request,'mainBook.html')



@login_required(login_url='login')
def lob(request):
    return render(request,'lobpics.html')

@login_required(login_url='login')

def pro(request):
    return render(request,'prgoics.html')

@login_required(login_url='login')
def nov(request):
    return render(request,'novpics.html')

@login_required(login_url='login')

def act(request):
    return render(request,'actionpics.html')

@login_required(login_url='login')

def support(request):
    return render(request,'support.html')

@login_required(login_url='login')
def readmore(request):
    return render(request,'readmore.html')


@login_required(login_url='login')
def contact(request):
    return render(request,'contact.html')



@login_required(login_url='login')
def sorry(request):
    return render(request,'sorry.html')

@login_required(login_url='login')
def payment(request):
    return render(request,'payment.html')

@login_required(login_url='login')
def paytm(request):
    return render(request,'paytm.html')


@login_required(login_url='login')
def gpay(request):
    return render(request,'gpay.html')

@login_required(login_url='login')
def ppay(request):
    return render(request,'ppay.html')

@login_required(login_url='login')
def ppal(request):
    return render(request,'ppal.html')