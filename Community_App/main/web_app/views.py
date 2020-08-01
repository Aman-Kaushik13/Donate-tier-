from django.shortcuts import render, redirect 
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from .models import CreatePage
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.utils import timezone

def registerPage(request):
    form = CreateUserForm()
    error = form.errors
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        error = form.errors
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            print(error)
    context = {'form':form,'error':error}

    return render(request, 'base.html',context)

def loginPage(request):
    return render(request, 'login.html')

def donatePage(request):
    donate = CreatePage.objects.all().order_by("-created_on")
    return render(request, 'searchbar.html', {
      "donate_items": donate
    })
    
def infoPage(request):
    return render(request ,'InfoPage.html')

def Create(request):
    current_date = timezone.now()
    description = request.POST.get("about")
    name = request.POST.get("content")
    location = request.POST.get("Location")
    created_obj = CreatePage.objects.create(created_on=current_date, description=description,location=location,organisation=name)
    return render(request,'create.html')

def CreatedPage(request,pk):

    create = CreatePage.objects.get(id=pk)
    context = {
        'create' : create,
    }
    return render(request, 'createdPage.html',context)