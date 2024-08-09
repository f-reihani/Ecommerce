from django.shortcuts import render, redirect
from .models import Product, Category
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .forms import SignupForm, UpdateUserForm

def category_summery(request):
    all_cat = Category.objects.all()
    return render(request, 'category_summery.html', {'category': all_cat})
def helloworld(request):
    all_products = Product.objects.all()
    return render(request, 'index.html', {'products': all_products})

def about(request):
    return render(request, 'about.html')

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, ("با موفقیت وارد شدید!"))
            return redirect("home")
        else:
            messages.success(request, ("مشکلی در لاکین وجود داشت"))
            return redirect("login")
    return render(request, 'login.html')

def logout_user(request):
    logout(request)
    messages.success(request, "با موفقیت خارج شدید!")
    return redirect("home")


def signup_user(request):
    form = SignupForm()
    if request.method == "POST":
       form = SignupForm(request.POST)
       if form.is_valid():
           form.save()
           username = form.cleaned_data['username']
           password1 = form.cleaned_data['password1']
           user = authenticate(request, username=username, password=password1)
           login(request, user)
           messages.success(request, "اکانت شما ساخته شد!")
           return redirect("home")
       else:
           print(form.errors)
           messages.success(request, ('مشکلی در ثبت نام شما وجود دارد.'))
           return redirect("signup")
    else:
        return render(request, 'signup.html', {'form': form})

def update_user(request):
    if request.user.is_authenticated:
        current_user = User.objects.get(id=request.user.id)
        user_form = UpdateUserForm(request.POST or None, instance=current_user)
        if user_form.is_valid():
            user_form.save()
            login(request, current_user)
            messages.success(request, 'پروفایل شما ویرایش شد.')
            return redirect('home')
        return render(request, 'update_user.html',{'user_form':user_form})
    else:
        messages.success(request, 'ابتدا باید لاکین شوید.')
        return redirect('home')
def product(request, pk):
    product = Product.objects.get(id=pk)
    return render(request, 'product.html', {'product': product})

def category(request, cat):
    cat = cat. replace("-", " ")
    try:
        category = Category.objects.get(name=cat)
        product = Product.objects.filter(category=category)
        return render(request, 'category.html', {'products': product, "category": category})
    except:
        messages.success(request, ('دسته بندی وجود ندارد'))
        return redirect("home")
