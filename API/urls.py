from rest_framework import urlpatterns
from django.conf.urls import url
from API import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns ={
    url(r'^api/alumno/$',views.AlumnoViewSet.as_view()),
    url(r'^api/profesor/$',views.ProfesorViewSet.as_view()),
    url(r'^api/curso/$',views.CursoViewSet.as_view()),
    url(r'^api/buscar_alumno/(?P<rut>.+)/$',views.AlumnoBuscarViewSet.as_view()),
    url(r'^api/buscar_profesor/(?P<rut>.+)/$',views.ProfesorBuscarViewSet.as_view()),
    url(r'^api/buscar_curso/(?P<rut>.+)/$',views.CursoBuscarViewSet.as_view()),
    url(r'^api/asistencia_crear/$',views.AsistenciaViewCreateSet.as_view()),
    url(r'^api/asistencia_listar/$',views.AsistenciaListarViewSet.as_view()),
    url(r'^api/conteo/$',views.conteo_asistencia),
    url(r'^api/alumno_api/$',views.AlumnoApi),
    url(r'^api/asistencia_api/$',views.AsistenciaApi),
}

urlpatterns= format_suffix_patterns(urlpatterns) 