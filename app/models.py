from django.db import models

# Create your models here.
class Productos(models.Model):
    Codigo=models.AutoField(primary_key=True)
    Nombre=models.CharField(max_length=200)
    Precio=models.FloatField()
    Descripcion=models.CharField(max_length=300)
    Stock=models.IntegerField()
    Imagen=models.ImageField(upload_to="Productos", null=True)
    
    def __int__(self):
       self.Codigo 