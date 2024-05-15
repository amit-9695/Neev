from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth import get_user_model
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
# login
def login_view(request):
    if request.method == 'POST':
        is_valid = True
        username = request.POST['username']
        password = request.POST['password']
        if len(username) == 0 or len(username) > 20:
            messages.error(request, "username must be between 1 and 20 characters")
            is_valid = False
        if len(password) == 0:
            messages.error(request, "password cannot be empty")
            is_valid = False
        # authenticate user
        if is_valid:
            user = authenticate(
                request, 
                username=username,
                password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "login successful")
                return redirect('home')
            else:
                messages.error(request, "login failed")
    return render(request, 'accounts/login.html')

# register
def register_view(request):
    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, "account created successfully")
        return redirect('login')
    return render(request,'accounts/register.html',{'form': form})

# logout
def logout_view(request):
    logout(request)
    messages.success(request, "logout successful")
    return redirect('home')