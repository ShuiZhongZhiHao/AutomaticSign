from django.urls import path

from . import views

urlpatterns = [
    path('checkoutUDID', views.checkoutUDID),
    path('file_down', views.file_down),
    path('mobileconfigFile_down', views.mobileconfigFile_down),
    path('mobileconfigFile_d', views.mobileconfigFile_d),
    path('receive', views.receive),
]
