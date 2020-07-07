from django.shortcuts import render, redirect
from django.http import HttpResponse

from .forms import Subscriber_Form
from .models import Subscriber
# Create your views here.

def home(request):
    if request.method == "POST":
        form = Subscriber_Form(request.POST)
        if form.is_valid():
            sub_error = False
            new_sub = form.save(commit=False)
            new_sub.save()
            context = {'form' :form, 'sub_error':sub_error}
            return render(request, 'home.html', context)
        else: 
            sub_error = True
    else:
        form = Subscriber_Form()
        sub_error = False
    context = {'form' :form, 'sub_error':sub_error}
    return render(request, 'home.html', context)


def dashboard(request):
    subscribers = Subscriber.objects.all()
    print(subscribers)
    count = 0
    for subscriber in subscribers:
        count = count + 1

    sub_total = subscribers.count()
    context = {'sub_total':sub_total, 'subscribers': subscribers, 'count':count}
    return render(request, 'dashboard.html', context)
