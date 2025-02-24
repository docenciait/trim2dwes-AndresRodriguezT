from django.urls import path  
from . import views  

urlpatterns = [
    path('lista_denuncias/', views.lista_denuncias, name='denuncias.lista_denuncias'),  
    path('crear_denuncia/', views.crear_denuncia, name='denuncias.crear_denuncia'), 
    path('editar_denuncias/<int:denuncia_id>/', views.editar_denuncia, name='denuncias.editar_denuncia'),  
    path('eliminar_denuncia/<int:denuncia_id>/', views.eliminar_denuncia, name='denuncias.eliminar_denuncia')
]
