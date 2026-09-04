from django.shortcuts import render, redirect

from .models import Zayavka
from .forms import CreateUserForm

# Create your views here.

def index(request):
    data = Zayavka.objects.all()
    return render(request, 'index.html', context={
        'zayavki': data
    })



def register(request):

    if(request.method == "POST"):
        form = CreateUserForm(request.POST)
        if(form.is_valid()):
            form.save()
            return redirect('/')
    else:
        form = CreateUserForm()
    return render(request, 'register.html', context={
        'form': form
    })