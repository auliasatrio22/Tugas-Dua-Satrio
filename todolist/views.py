from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from todolist.models import Task
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.core import serializers
from django.http import JsonResponse
from datetime import date
from todolist.forms import TaskForm

# Create your views here.
@login_required(login_url='/todolist/login/')
def show_todolist(request):
    data_todolist = Task.objects.filter(user=request.user)
    context = {
    'list_todolist': data_todolist,
    'nama': request.user,
}
    return render(request, "todolist.html", context)

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('todolist:login')
    
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('todolist:show_todolist')
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    return redirect('todolist:login')

def add_task(request):
    if request.method == "POST":
        task = Task(user=request.user,  date=date.today())
        form = TaskForm(request.POST or None, instance=task)
        if form.is_valid():
            form.save()
            return redirect('todolist:show_todolist')
    return render(request, 'addTask.html')

def get_json(request):
    new_data = Task.objects.filter(user=request.user)
    return HttpResponse(
            serializers.serialize("json", new_data),
            content_type="application/json")