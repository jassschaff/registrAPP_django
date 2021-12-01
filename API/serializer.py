from .models import Alumno,Profesor,Asistencia,Curso
from rest_framework import serializers

class AlumnoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alumno
        fields = ["rut_alumno","nombre_alu","user_alu","pass_alu"]

class ProfesorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profesor
        fields = ["rut_pro","nombre_pro","user_pro","pass_pro"]

class AsistenciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asistencia
        fields = ["id","fecha","hora","profesor_rut_pro","alumno_rut_alumno","curso_seccion"]

class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = ["seccion","horario","dia","curso","id","profesor_rut_pro"]

