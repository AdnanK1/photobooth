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
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('home')
    context = {'form':form}
    return render(request,'register.html',context)

def login(request):
    context = {}
    return render(request,'login.html',context)
