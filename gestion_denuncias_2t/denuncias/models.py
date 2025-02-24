from django.db import models

# Create your models here.
class Denuncia(models.Model):
  id = models.AutoField(primary_key=True)
  titulo = models.CharField(max_length=255)
  descripcion = models.TextField()
  imagen = models.ImageField()
  categoria = models.CharField(max_length=100)
  estado = models.CharField(max_length=100)
  fecha_creacion = models.TimeField(auto_now_add=True)
  

  def __str__(self):
      return str(self.titulo)