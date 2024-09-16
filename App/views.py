from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
from .models import Group

# Create your views here.
def homepageview(request):
    return render(request, 'home.html')

def errorview(request):
    return render(request, 'error.html')


def register(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('homepage')
    else:
        form = UserForm()
    return render(request, 'register.html', {"form":form})


def LoginView(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = User.objects.filter(username=username, password=password)
            if user:
                return redirect('homepage')
            else:
                    return redirect('error')
    else:
        form = LoginForm()
    return render(request, 'login.html', {"form":form})



def creategroupview(request):
    if request.method == 'POST':
        form = GroupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('homepage')
        else:
            return redirect('error')
    else:
        form = GroupForm()
    return render(request, 'creategroup.html', {"form":form})        



def group_by_name(request):
    name = request.GET.get('name', '')
    if name:
        group = get_object_or_404(Group, name=name)
        return render(request, 'group_detail.html', {'group': group})
    else:
        return redirect('error')

