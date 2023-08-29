from django.shortcuts import render, redirect
from .forms import CustomAuthenticationForm, CustomerUserCreationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout

# Create your views here.

def signup(request):
    if request.user.is_authenticated():
        return redirect('articles:index')
    
    if request.method == 'POST':
        form = CustomerUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            print(user, user.username, user.password)
            auth_login(request, user)
            return redirect('accounts:index')
        
    else:
        form = CustomerUserCreationForm()
            
            
    context = {
        'form': form,
    }
    return render(request, 'signup.html', context)


def login(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            
            next_url = request.GET.get('next')
            
            return redirect(next_url or 'accounts:index')
        
    else:
        form = CustomAuthenticationForm()
        
    context = {
        'form': form,
    }
    
    return render(request, 'login.html', context)


def logout(request):
    auth_logout(request)
    return redirect('accounts:login')
