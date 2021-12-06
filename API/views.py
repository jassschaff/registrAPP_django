from django.shortcuts import render
from typing import ParamSpec
from django.db.models.query import QuerySet
from .serializer import AlumnoSerializer, ProfesorSerializer,AsistenciaSerializer,CursoSerializer
from rest_framework import generics, serializers
from .models import Alumno,Profesor,Asistencia,Curso

# Create your views here.

# importante
from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser

#--------------------------



class AlumnoViewSet(generics.ListAPIView):
    queryset = Alumno.objects.all()
    serializer_class = AlumnoSerializer

class ProfesorViewSet(generics.ListAPIView):
    queryset = Profesor.objects.all()
    serializer_class = ProfesorSerializer

class CursoViewSet(generics.ListAPIView):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer

######

class AlumnoBuscarViewSet(generics.ListAPIView):
    serializer_class = AlumnoSerializer
    def get_queryset(self):
        elrut=self.kwargs["rut"]
        return Alumno.objects.filter(rut_alumno=elrut)

class ProfesorBuscarViewSet(generics.ListAPIView):
    serializer_class = ProfesorSerializer
    def get_queryset(self):
        elrut=self.kwargs["rut"]
        return Profesor.objects.filter(rut_pro=elrut)

class CursoBuscarViewSet(generics.ListAPIView):
    serializer_class = CursoSerializer
    def get_queryset(self):
        elrut=self.kwargs["rut"]
        ##print(elrut)
        return Curso.objects.filter(profesor_rut_pro=elrut)

######

class AsistenciaViewCreateSet(generics.CreateAPIView):
    querySet = Asistencia.objects.all()
    serializer_class = AsistenciaSerializer

class AsistenciaListarViewSet(generics.ListAPIView):
    queryset = Asistencia.objects.all()
    serializer_class = AsistenciaSerializer



@csrf_exempt
def AlumnoApi(request):
    if request.method=='GET':
        Alumnos = Alumno.objects.all()
        alumno_serializar = AlumnoSerializer(Alumnos,many=True)
        return JsonResponse(alumno_serializar.data,safe=False)
    if request.method=='POST':
        alumno_data= JSONParser().parse(request)
        alumno_serializar = AlumnoSerializer(data=alumno_data)
        if alumno_serializar.is_valid():
            alumno_serializar.save()
            return JsonResponse("Agrego persona",safe=False)
        return JsonResponse("No pudo agregar",safe=False)
    if request.method=='DELETE':
        try:
            alumno = Alumno.objects.get(rut=id)
            alumno.delete()
            return JsonResponse("elimino",safe=False)
        except:
            return JsonResponse("no pudo eliminar",safe=False)
    if request.method=='PUT':
        alumno_data= JSONParser().parse(request)
        alumno = Alumno.objects.get(rut= alumno_data['rut'])
        alumno_serializar = AlumnoSerializer(alumno,data=alumno_data)
        if alumno_serializar.is_valid():
            alumno_serializar.save()
            return JsonResponse("modifico",safe=False)
        return JsonResponse("no modifico",safe=False)


@csrf_exempt
def ProfesorApi(request):
    if request.method=='GET':
        profesores = Profesor.objects.all()
        profesor_serializar = ProfesorSerializer(profesores,many=True)
        return JsonResponse(profesor_serializar.data,safe=False)
    if request.method=='POST':
        profesor_data= JSONParser().parse(request)
        profesor_serializar = ProfesorSerializer(data=profesor_data)
        if profesor_serializar.is_valid():
            profesor_serializar.save()
            return JsonResponse("Agrego persona",safe=False)
        return JsonResponse("No pudo agregar",safe=False)
    if request.method=='DELETE':
        try:
            profesor = Profesor.objects.get(rut=id)
            profesor.delete()
            return JsonResponse("elimino",safe=False)
        except:
            return JsonResponse("no pudo eliminar",safe=False)
    if request.method=='PUT':
        profesor_data= JSONParser().parse(request)
        profesor = Profesor.objects.get(rut= profesor_data['rut'])
        profesor_serializar = ProfesorSerializer(profesor,data=profesor_data)
        if profesor_serializar.is_valid():
            profesor_serializar.save()
            return JsonResponse("modifico",safe=False)
        return JsonResponse("no modifico",safe=False)


@csrf_exempt
def AsistenciaApi(request):
    if request.method=='GET':
        asistencias = Asistencia.objects.all()
        asistencia_serializar = AsistenciaSerializer(asistencias,many=True)
        return JsonResponse(asistencia_serializar.data,safe=False)
    if request.method=='POST':
        asistencia_data= JSONParser().parse(request)
        asistencia_serializar = AsistenciaSerializer(data=asistencia_data)
        if asistencia_serializar.is_valid():
            asistencia_serializar.save()
            return JsonResponse("Agrego persona",safe=False)
        return JsonResponse("No pudo agregar",safe=False)
    if request.method=='DELETE':
        try:
            asistencia = Asistencia.objects.get(rut=id)
            asistencia.delete()
            return JsonResponse("elimino",safe=False)
        except:
            return JsonResponse("no pudo eliminar",safe=False)
    if request.method=='PUT':
        asistencia_data= JSONParser().parse(request)
        asistencia = Asistencia.objects.get(rut= asistencia_data['rut'])
        asistencia_serializar = AsistenciaSerializer(asistencia,data=asistencia_data)
        if asistencia_serializar.is_valid():
            asistencia_serializar.save()
            return JsonResponse("modifico",safe=False)
        return JsonResponse("no modifico",safe=False)


@csrf_exempt
def conteo_asistencia(request):
    if request.method=='POST':
        cantidad = Asistencia.objects.all().count()
        return JsonResponse(cantidad,safe=False)
    return JsonResponse(0,safe=False)


