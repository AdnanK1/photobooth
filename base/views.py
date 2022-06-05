from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
# Create your views here.
def home(request):
    context = {}
    return render(request,'home.html',context)

def register(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form':form}
    return render(request,'register.html',context)

def login(request):
    context = {}
    return render(request,'login.html',context)
