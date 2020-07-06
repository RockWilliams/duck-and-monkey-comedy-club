from django.shortcuts import render
from django.http import HttpResponse

from .forms import Subscriber_Form
# Create your views here.

def home(request):
    form = Subscriber_Form()
    context = {'form' :form}
    return render(request, 'home.html', context)


def dashboard(request):
    return render(request, 'dashboard.html')
