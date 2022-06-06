from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout 
from django.db.models import Q
from .forms import CreateUserForm, CreatePost
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
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            email = form.cleaned_data['email']
            #recipient = NewsLetterRecipients(username=username,email=email)
            user = authenticate(username=username,password=password)
            login(request,user)
            return redirect('home')

    context = {'form':form}
    return render(request,'auth/register.html',context)

def login_page(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = User.objects.get(username=username)
        except: 
            messages.error(request, 'User does not exist ')

        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.error(request, 'Username or Password does not exist')

    context = {}
    return render(request,'auth/login.html',context)

def logoutUser(request):
    logout(request)
    return redirect('login')

def createPost(request):
    form = CreatePost()
    context = {'form':form}
    return render(request,'create_post.html',context)
