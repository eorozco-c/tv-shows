from django.http.response import HttpResponse
from django.shortcuts import redirect, render,HttpResponse
from .models import Show
import datetime

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
        title = request.POST["title"]
        network = request.POST["network"]
        releaseDate = request.POST["releaseDate"]
        description = request.POST["description"]
        Show.objects.create(title=title,network=network,release_date=releaseDate,description=description)
    lastshow = Show.objects.last()
    return redirect(f"/shows/{lastshow.id}")

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
        show = Show.objects.get(id=id)
        show.title = request.POST["title"]
        show.network = request.POST["network"]
        show.releaseDate = request.POST["releaseDate"]
        show.description = request.POST["description"]
        show.save()
    return redirect(f"/shows/{show.id}")

def destroy(request,id):
    show = Show.objects.get(id=id)
    show.delete()
    return redirect("/")