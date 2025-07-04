from django.db import models
from django.core.validators import MinValueValidator
from applications.commons.models import AuditModel

class Film(AuditModel):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class Character(AuditModel):
    """
    Modelo para personajes de Star Wars.
    """
    name = models.CharField(max_length=100)
    height = models.IntegerField(validators=[MinValueValidator(0)], help_text="Altura en centímetros")
    mass = models.FloatField(validators=[MinValueValidator(0)], help_text="Masa en kilogramos")
    hair_color = models.CharField(max_length=50)
    gender = models.CharField(max_length=10)
    homeworld = models.CharField(max_length=100)
    dob = models.DateField(help_text="Fecha de nacimiento")
    img = models.URLField(help_text="URL de la imagen/avatar del personaje")
    films = models.ManyToManyField(Film)

    def __str__(self):
        return self.name
