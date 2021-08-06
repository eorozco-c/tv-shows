from django.db import models
import datetime

# Create your models here.
class ShowManager(models.Manager):
    def basic_validator(self, postData,tipo=None):
        errors = {}
        release_date =  datetime.datetime.strptime(postData['release_date'], '%Y-%m-%d').date()
        today = datetime.date.today()
        if len(postData['title']) < 2:
            errors["title"] = "El titulo debe tener minimo 2 caracteres"
        if len(postData['network']) < 3:
            errors["network"] = "Network debe tener minimo 3 caracteres"
        if len(postData['description']) < 10 and postData['description'] != "":
            errors["description"] = "Description debe tener minimo 10 caracteres"
        if  release_date >= today:
            #print(release_date, today)
            errors["release_date"] = "Fecha debe ser menor al dia de hoy"
        show = self.filter(title__iexact=postData['title'])
        if show.exists() and tipo == "create":
            errors["title"] = "Ya existe ese titulo"
        return errors

class Show(models.Model):
    title = models.CharField(max_length=50)
    network = models.CharField(max_length=20)
    release_date = models.DateField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ShowManager()

