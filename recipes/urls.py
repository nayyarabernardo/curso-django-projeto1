from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('recipes/<int:id>/', views.recipe),
    #teste HUPDATA
    path('teste/', views.teste),
    path('teste/atualizar_serie/', views.atualizar_serie),

]
