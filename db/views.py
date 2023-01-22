from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import *
from .models import *
from django.views.decorators.csrf import requires_csrf_token

@requires_csrf_token
def home_page(request):
    form = emp_form()
    if request.method == 'POST':
        form = emp_form(request.POST, request.FILES)
        if form.is_valid():
            print("is valid")
            form.save()
            return redirect('emp details')
        print("is not vallid")
    context = {
        'form': form,
    }
    return render(request, "home.html", context)

@requires_csrf_token
def emp_details(request):
    form = Employee.objects.all()
    print(form)

    context = {
        'form': form
    }
    return render(request, "emp_details.html", context)