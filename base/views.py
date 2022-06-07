from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout 
from django.db.models import Q
from .forms import CreateUserForm, CreatePost,UpdateUserForm, UpdateProfileForm
from .models import Image
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse


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

@login_required
def createPost(request):
    form = CreatePost()
    if request.method == 'POST':
        form = CreatePost()
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form':form}
    return render(request,'create_post.html',context)


def PostLike(request,pk):
    post = get_object_or_404(Image, id=request.POST.get('Image_id'))
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)

