from django.contrib import admin
from .models import Alumno,Asistencia,Curso,Profesor


# Register your models here.
# para que aparesca en el admin de losthoes
admin.site.register(Alumno)
admin.site.register(Asistencia)
admin.site.register(Curso)
admin.site.register(Profesor)