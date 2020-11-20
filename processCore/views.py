from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.http import HttpResponse
from django import template
from .models import *
from processAuth.models import userModel
from .forms import *
from django.db.models import Q

@login_required(login_url="/login/")
def client_list(request):
    current_user = request.user
    
    context = {}
    context['client_list'] = Client.objects.all()
    context['employee'] = userModel.objects.get(user=current_user)
    
    return render(request, 'index.html', context=context)

def unidad_list(request, client_pk):
    current_user = request.user

    context = {}
    context['client'] = Client.objects.get(pk=client_pk)
    context['unidad_list'] = UnidadInterna.objects.filter(client=client_pk)
    context['employee'] = userModel.objects.get(user=current_user)

    return render(request, 'unidad_list.html', context=context)

def listado_flujo(request, client_pk, process_pk):
    current_user = request.user

    context = {}
    context['client'] = Client.objects.get(pk=client_pk)
    context['process'] = Process.objects.get(pk=process_pk)
    context['flujo_list'] = FlujoTareas.objects.filter(process=process_pk)   
    context['employee'] = userModel.objects.get(user=current_user) 

    return render(request, 'flujo_list.html', context=context)

def agregar_flujo(request, client_pk, process_pk):

    if request.method == 'POST':
        form = flujoForm(request.POST)
        
        if form.is_valid():
            FlujoTareas = form.save(commit=False)
            FlujoTareas.process = Process.objects.get(pk=process_pk)
            FlujoTareas.save()
            
            return redirect('listado_flujo', client_pk=client_pk, process_pk=process_pk)

    else:
        form = flujoForm()

    context = {}
    context['client'] = Client.objects.get(pk=client_pk)
    context['process'] = Process.objects.get(pk=process_pk)
    context['task'] = Task.objects.all()    
    context['form'] = form

    return render(request, 'forms/agregar_flujo.html', context=context)


def agregar_unidad(request, client_pk):
    if request.method == 'POST':
        form = unidadForm(request.POST)
        
        if form.is_valid():
            UnidadInterna = form.save(commit=False)
            UnidadInterna.client = Client.objects.get(pk=client_pk)
            UnidadInterna.save()
            
            return redirect('unidad_list', client_pk=client_pk)

    else:
        form = unidadForm()

    context = {}
    context['client'] = Client.objects.get(pk=client_pk)    
    context['form'] = form

    return render(request, 'forms/agregar_unidad.html', context=context)

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
        
        if "accept_task" in request.POST:
            task = get_object_or_404(Task, id=request.POST['taskpk'])
            task.status = 1
            task.save()
            return redirect('process_detail', client_pk=client_pk, process_pk=process_pk)   
                
    context = {}
    context['client'] = Client.objects.get(pk=client_pk)
    context['process'] = Process.objects.get(pk=process_pk)
    context['task_list'] = Task.objects.filter(process=process_pk).order_by('-created_at')
    context['employee'] = userModel.objects.get(user=current_user)
    context['comment_list'] = Rejectcomment.objects.all()

    context['finished_task'] = finished
    context['inprogress_task'] = Task.objects.filter( Q(status=1, process=process_pk) | Q(status=4, process=process_pk) | Q(status=3, process=process_pk)).count()
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

def subordinada_list(request, client_pk, process_pk, task_pk):
    current_user = request.user

    context = {}
    context['client'] = Client.objects.get(pk=client_pk)
    context['process'] = Process.objects.get(pk=process_pk)
    context['employee'] = userModel.objects.get(user=current_user)
    context['task'] = Task.objects.get(pk=task_pk)
    context['subordinada_list'] = TareaSubordinada.objects.filter(task=task_pk)

    return render(request, 'subordinada_list.html', context=context)

def agregar_subordinada(request, client_pk, process_pk, task_pk):

    if request.method == 'POST':
        form = subordinadaForm(request.POST)
        
        if form.is_valid():
            TareaSubordinada = form.save(commit=False)
            TareaSubordinada.task = Task.objects.get(pk=task_pk)
            TareaSubordinada.save()
            
            return redirect('process_detail', client_pk=client_pk, process_pk=process_pk)

    else:
        form = subordinadaForm()

    context = {}
    context['client'] = Client.objects.get(pk=client_pk)
    context['process'] = Process.objects.get(pk=process_pk)
    context['task'] = Task.objects.get(pk=task_pk)
    context['form'] = form

    return render(request, 'forms/agregar_subordinada.html', context=context)


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


def reject_task(request, client_pk, process_pk, task_pk):

    current_user = request.user
    taskStatus = get_object_or_404(Task, pk = task_pk)

    if request.method == 'POST':
        form = commentForm(request.POST)

        if form.is_valid():
            Comment = form.save(commit=False)
            Comment.responsable = userModel.objects.get(name=current_user)
            Comment.task = Task.objects.get(pk=task_pk)
            Comment.save()

            taskStatus.status = 3
            taskStatus.save()

            return redirect('process_detail', client_pk=client_pk, process_pk=process_pk)

    else:
        form = commentForm()

    context = {}
    context['task'] = Task.objects.get(pk=task_pk)
    context['process'] = Process.objects.get(pk=process_pk)
    context['client'] = Client.objects.get(pk=client_pk)
    context['form'] = form

    return render(request, 'forms/reject_comment.html', context=context)

def detail_reject(request, client_pk, process_pk, task_pk, reject_pk):

    if request.method == 'POST':

        if "delete_task" in request.POST:
            instance = Rejectcomment.objects.get(pk=reject_pk)
            instance.delete()

            instance = Task.objects.get(pk=task_pk)
            instance.delete()

            return redirect('process_detail', client_pk=client_pk, process_pk=process_pk)
 
    context = {}
    context['edite'] = taskForm
    context['comment'] = Rejectcomment.objects.get(pk=reject_pk)
    context['task'] = Task.objects.get(pk=task_pk)
    context['process'] = Process.objects.get(pk=process_pk)
    context['client'] = Client.objects.get(pk=client_pk)

    return render(request, 'comment_detail.html', context=context)

def problema_list(request):
    current_user = request.user

    context = {}
    context['problema_list'] = ProblemaTarea.objects.all()    

    return render(request, 'problema_list.html', context=context)

def reportar_problema(request, client_pk, process_pk, task_pk):

    if request.method == 'POST':
        form = problemaForm(request.POST)
        
        if form.is_valid():
            ProblemaTarea = form.save(commit=False)
            ProblemaTarea.tarea = Task.objects.get(pk=task_pk)
            ProblemaTarea.save()
            
            return redirect('process_detail', client_pk=client_pk, process_pk=process_pk)

    else:
        form = problemaForm()

    context = {}
    context['client'] = Client.objects.get(pk=client_pk)
    context['process'] = Process.objects.get(pk=process_pk)
    context['task'] = Task.objects.get(pk=task_pk)
    context['form'] = form

    return render(request, 'forms/reportar_problema.html', context=context)