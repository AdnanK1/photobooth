from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.db.models import Q
from .forms import CreateUserForm
from .models import Image

# Create your views here.
def home(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    images = Image.objects.filter(
        Q(name__icontains=q) |
        Q(caption__icontains=q) 
    )

    context = {'images':images}
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
