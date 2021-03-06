from os import error
from django.http import JsonResponse
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from .models import Show
from django.contrib import messages

# Create your views here.
def root(request):
   return redirect("/shows")

def index(request):
    if request.method == "GET":
        context = {
            "shows" : Show.objects.exclude(network="TV").all(),
            "tvs" : Show.objects.filter(network="TV").all(),
        }
    return render(request, "index.html", context)

def new(request):
   return render(request, "new.html")

def create(request):
    if request.method == "POST":
        errors = Show.objects.basic_validator(request.POST,"create")
        if len(errors) > 0:
            return JsonResponse(errors)
        title = request.POST["title"]
        network = request.POST["network"]
        release_date = request.POST["release_date"]
        description = request.POST["description"]
        lastshow = Show.objects.create(title=title,network=network,release_date=release_date,description=description)
        return JsonResponse({"resultado": lastshow.id })
        #return redirect(f"/shows/{lastshow.id}")
        

def shows(request,id):
    if request.method == "GET":
        context = {
            "show" : Show.objects.get(id=id),
        }
    return render(request, "show.html", context)

def edit(request,id):
    if request.method == "GET":
        context = {
            "show" : Show.objects.get(id=id),
        }
    return render(request, "edit.html", context)

def update(request,id):
    if request.method == "POST":
        errors = Show.objects.basic_validator(request.POST)
        if len(errors) > 0:
            return JsonResponse(errors)
            #for key, value in errors.items():
             #   messages.error(request, value)
            # redirigir al usuario al formulario para corregir los errores
            #return redirect(f'/shows/{id}/edit')
        show = Show.objects.get(id=id)
        show.title = request.POST["title"]
        show.network = request.POST["network"]
        show.release_date = request.POST["release_date"]
        show.description = request.POST["description"]
        show.save()
        return JsonResponse({"resultado": show.id })
        #return redirect(f"/shows/{show.id}")

def destroy(request,id):
    show = Show.objects.get(id=id)
    show.delete()
    return redirect("/")

def validate(request):
    title = request.GET.get('title', None)
    data = {
        'title': Show.objects.filter(title__iexact=title).exists()
    }
    return JsonResponse(data)