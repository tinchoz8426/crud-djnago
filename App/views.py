from django.shortcuts import redirect, render

from .models import Task

# Create your views here.


def index(request):
    # tasks = Task.objects.order_by("-id") # filtro y ordeno por ID descendente
    # Ordeno del ultimo al primero con slicing
    tasks = Task.objects.all()[::-1]
    context = {"tasks": tasks}
    return render(request, "apps/index.html", context)


def insert(request):
    try:
        task_subject = request.POST["subject"].capitalize()
        task_description = request.POST["description"].capitalize()

        if task_subject == "" or task_description == "":
            raise ValueError("El texto no puede estar vacio")

        tasks = Task(subject=task_subject, description=task_description)
        tasks.save()
        return redirect("Index")
    except ValueError as e:
        print(e)
    return redirect("Index")


def update_form(request, task_id):
    # tasks = Task.objects.all()
    task_update = Task.objects.get(pk=task_id)
    context = {"task_update": task_update, }
    return render(request, "apps/index.html", context)

def update(request):
    task_id = request.POST["id"]
    task_subject = request.POST["subject"]
    task_description = request.POST["description"]
    task_update = Task.objects.get(pk=task_id)
    task_update.subject = task_subject 
    task_update.description = task_description 
    task_update.save()
    return redirect("Index")

def delete(request, task_id):
    task = Task.objects.filter(id=task_id)
    task.delete()
    return redirect("Index")