from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.http import HttpResponse
from django import template
from .models import *
from processAuth.models import userModel
from .forms import *

@login_required(login_url="/login/")
def client_list(request):
    current_user = request.user
    
    context = {}
    context['client_list'] = Client.objects.all()
    context['employee'] = userModel.objects.get(user=current_user)
    
    return render(request, 'index.html', context=context)


def process_list(request, client_pk):
    current_user = request.user

    context = {}
    context['client'] = Client.objects.get(pk=client_pk)
    context['process_list'] = Process.objects.filter(client=client_pk)
    context['employee'] = userModel.objects.get(user=current_user)

    return render(request, 'process_list.html', context=context)


def process_detail(request, client_pk, process_pk):
    current_user = request.user

    finished = Task.objects.filter(status=0, process=process_pk).count()
    total = Task.objects.filter(process=process_pk).count()

    if(total != 0):
        percentage = round((finished * 100)/total)
    else:
        percentage = 0

    if request.method == "POST":
        if "finish_task" in request.POST:
            task = get_object_or_404(Task, id=request.POST['taskpk'])
            task.status = 0
            task.save()
            return redirect('process_detail', client_pk=client_pk, process_pk=process_pk)
                
    context = {}
    context['client'] = Client.objects.get(pk=client_pk)
    context['process'] = Process.objects.get(pk=process_pk)
    context['task_list'] = Task.objects.filter(process=process_pk).order_by('-created_at')
    context['employee'] = userModel.objects.get(user=current_user)

    context['finished_task'] = finished
    context['inprogress_task'] = Task.objects.filter(status=1, process=process_pk).count()
    context['expired_task'] = Task.objects.filter(status=2, process=process_pk).count()
    context['all_task'] = total
    context['percentage'] = percentage

    return render(request, 'process_detail.html', context=context)


def add_task(request, client_pk, process_pk):

    if request.method == 'POST':
        form = taskForm(request.POST)
        
        if form.is_valid():
            Task = form.save(commit=False)
            Task.process = Process.objects.get(pk=process_pk)
            Task.save()
            
            return redirect('process_detail', client_pk=client_pk, process_pk=process_pk)

    else:
        form = taskForm()

    context = {}
    context['client'] = Client.objects.get(pk=client_pk)
    context['process'] = Process.objects.get(pk=process_pk)
    context['form'] = form

    return render(request, 'forms/add_task.html', context=context)


def add_process(request, client_pk):

    if request.method == 'POST':
        form = processForm(request.POST)
        
        if form.is_valid():
            Process = form.save(commit=False)
            Process.client = Client.objects.get(pk=client_pk)
            Process.save()
            
            return redirect('process_list', client_pk=client_pk)

    else:
        form = processForm()

    context = {}
    context['client'] = Client.objects.get(pk=client_pk)
    context['form'] = form

    return render(request, 'forms/add_process.html', context=context)


def add_client(request):

    if request.method == 'POST':
        form = clientForm(request.POST)
        
        if form.is_valid():
            Client = form.save(commit=False)
            Client.save()
            
            return redirect('client_list')

    else:
        form = processForm()

    context = {}
    context['form'] = form

    return render(request, 'forms/add_client.html', context=context)
