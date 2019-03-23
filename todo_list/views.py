from django.shortcuts import render, redirect
from .models import List
from .forms import ListForm
from django.contrib import messages
from django.http import HttpResponseRedirect


# Create your views here.
def home(request):
    if request.method == 'POST':
        form = ListForm(request.POST or None)

        if form.is_valid():
            form.save()
            all_items = List.objects.all
            context = {'all_items': all_items}
            messages.success(request, "Item has been added to List! ")
            return render(request, 'home.html', context)
    else:
        all_items = List.objects.all
        context = {'all_items': all_items}
        return render(request, 'home.html', context)


# about page
def about(request):
    return render(request, 'about.html', {"name": 'Masila'})


# delete route
def delete(request, list_id):
    item = List.objects.get(pk=list_id)
    item.delete()
    messages.success(request, "Item has been deleted from List! ")
    return redirect('home')
