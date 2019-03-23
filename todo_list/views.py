from django.shortcuts import render
from .models import List
from .forms import ListForm


# Create your views here.
def home(request):
    all_items = List.objects.all
    context = {'all_items': all_items}
    return render(request, 'home.html', context)


# about page
def about(request):
    return render(request, 'about.html', {"name": 'Masila'})
