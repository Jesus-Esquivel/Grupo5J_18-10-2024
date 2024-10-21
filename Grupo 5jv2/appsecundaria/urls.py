from django.urls import path
from appsecundaria import views


urlpatterns = [
  path("",views.Index_vista,name="index_vista"),

  path('alumno/<int:id>',views.Alumno_vista)
]
