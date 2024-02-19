from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth import views as auth_views
from django.contrib.auth.models import User
from quiz.forms import LoginForm, RegisterForm, AccForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from quiz.models import Account
from django.contrib.auth.decorators import login_required
def register(request):
    form = RegisterForm()
    if request.method == "POST":
         form = RegisterForm(request.POST)
         #check if form is valid
         if form.is_valid():
             form.save()
             username = request.POST.get('username')
             password = form.cleaned_data['password2']
             #creating the account from models
             user = authenticate(username=username,password=password)
             login(request, user)
             
             return redirect('home')
    else:
         form = RegisterForm()
    return render(request,'register.html',{'form':form})

def login_view(request):
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(request,request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password= request.POST.get('password')
            user = authenticate(request,username=username,password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                print("Authentication failed. Invalid username or password.")
    return render(request,'login.html',{'form':form})    
# @login_required(login_url='login')

def home(request):
    account = Account.objects.order_by('name')
    p = Paginator(account,3)
    page = request.GET.get('page')
    try:
        pages = p.get_page(page)  # returns the desired page object
    except PageNotAnInteger:
        # if page_number is not an integer then assign the first page
        pages = p.page(1)
    except EmptyPage:
        # if page is empty then return last page
        pages = p.page(p.num_pages)
    # pages = p.get_page(page)
    return render(request,'home.html',{'account':account,'pages':pages})
def search(request):
    account = None
    if request.method == "POST":
        searchs = request.POST.get('search')
        account = Account.objects.filter(name__icontains=searchs)
    return render(request,'search.html',{'account':account})
def addForm(request):

    form = AccForm()
    if request.method == "POST":
        form = AccForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request,'add.html',{'form':form})
def delet(request,id):
    objectss = get_object_or_404(Account,id=id)
    objectss.delete()
    return redirect('home')
def updat(request,id):
    
    account = get_object_or_404(Account,id=id)
    form = AccForm(instance=account)
    if request.method == "POST":
        form = AccForm(request.POST, instance=account)
        if form.is_valid():
           form.save()
           return redirect('home')
    return render(request,'add.html',{'form':form})

