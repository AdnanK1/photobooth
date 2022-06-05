from operator import concat
from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def home(request):
    context = {}
    return render(request,'home.html',context)

def register(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form':form}
    return render(request,'register.html',context)

def login(request):
    context = {}
    return render(request,'login.html',context)
