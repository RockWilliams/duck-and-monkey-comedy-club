from django.shortcuts import render, redirect
from django.http import HttpResponse

from .forms import Subscriber_Form
from .models import Subscriber
# Create your views here.

def home(request):
    if request.method == "POST":
        form = Subscriber_Form(request.POST)
        if form.is_valid():
            new_sub = form.save(commit=False)
            new_sub.save()
            return redirect('home')
    else:
        form = Subscriber_Form()
    context = {'form' :form}
    return render(request, 'home.html', context)


def dashboard(request):
    return render(request, 'dashboard.html')
