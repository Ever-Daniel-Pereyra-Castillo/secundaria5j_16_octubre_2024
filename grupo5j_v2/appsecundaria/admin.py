from django.contrib import admin
from .models import AlumnoT,Frase
# Register your models here.



class ComentarioInline(admin.TabularInline):
    model=Frase
    extra=1
    
class AlumnoAdmin(admin.ModelAdmin):
    fields=["Apaterno","Amaterno","Nombre","Fecha_nacimiento","Fecha_ingreso"]
    list_display=["Apaterno","Amaterno","Nombre"]
    inlines=[ComentarioInline]
    
admin.site.register(AlumnoT,AlumnoAdmin)

@admin.register(Frase)
class FraseAdmin(admin.ModelAdmin):
    fields=["comentario","Alumno_fk"]
    list_display=["comentario"]