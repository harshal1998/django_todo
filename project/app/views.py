from django.shortcuts import render, redirect
from .forms import *


# Create your views here.
def a(request):
    form = todoform()
    if request.method == 'POST':
        data = todoform(request.POST)
        if data.is_valid():
            data.save()
    dbdata = todo.objects.all()
    data1 = {
        'form': form,
        'data': dbdata,
    }
    return render(request, 'home.html', data1)


def delete(request, id):
    print(id)
    data = todo.objects.get(id=id)
    print(data)
    data.delete()
    return redirect('/')


def cross(request, id):
    data = todo.objects.get(id=id)
    data.completed = True
    data.save()
    return redirect("/")


def uncross(request, id):
    data = todo.objects.get(id=id)
    data.completed = False
    data.save()
    return redirect("/")
