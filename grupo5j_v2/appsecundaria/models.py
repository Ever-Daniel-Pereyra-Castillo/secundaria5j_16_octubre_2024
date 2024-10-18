from django.db import models

# Create your models here.

class AlumnoT(models.Model):
    Apaterno=models.CharField(max_length=50,verbose_name="Apellido Paterno")
    Amaterno=models.CharField(max_length=50,verbose_name="Apellido Materno")
    Nombre=models.CharField(max_length=50,verbose_name="Nombre(s)")
    Fecha_nacimiento=models.DateField(verbose_name="Fecha De Nacimiento", null=False, blank=False)
    Fecha_ingreso=models.DateField(verbose_name="Fecha De Ingreso", null=False, blank=False)
    
    class Meta:
        db_table = 'Alumnos'
        verbose_name = 'Alumno'
        verbose_name_plural = 'Alumnos'
    
    def __str__(self) -> str:
        return self.Nombre
    
    
class Frase(models.Model):
    comentario=models.TextField(verbose_name='Comentario',max_length=400)
    Alumno_fk=models.ForeignKey(AlumnoT, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = 'Frase'
        verbose_name_plural = 'frases'
    def __str__(self) -> str:
        return self.comentario
    