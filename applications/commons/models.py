from django.db import models
from django.utils import timezone

# Create your models here.

class AuditModel(models.Model):
    usuario_mod = models.CharField(max_length=30)
    fecha_mod = models.DateField(default=timezone.now)
    activo = models.IntegerField(default=1)

    class Meta:
        abstract = True
