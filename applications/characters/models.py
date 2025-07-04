from django.db import models
from applications.commons.models import AuditModel

# Create your models here.
class Film(AuditModel):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class Character(AuditModel):
    name = models.CharField(max_length=100)
    height = models.IntegerField()
    mass = models.FloatField()   
    hair_color = models.CharField(max_length=50)
    gender = models.CharField(max_length=10)
    homeworld = models.CharField(max_length=100)
    dob = models.CharField(max_length=50)  
    img = models.URLField()
    films = models.ManyToManyField(Film)

    def __str__(self):
        return self.name
