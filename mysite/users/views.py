from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import RegistrationForm
from django.contrib.auth.decorators import login_required


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username').capitalize()
            messages.success(request,f'Welcome {username} Hurrayyy!!! Your account is successfully created')
            form.save()
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request,'users/register.html',{'form':form})

@login_required
def profilepage(request):
    return render(request,'users/profile.html')