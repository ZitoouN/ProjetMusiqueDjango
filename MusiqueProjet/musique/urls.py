from django.urls import path
from . import views

urlpatterns = [
        path('ajout/', views.ajout),
        path('ajout2/', views.ajout2),
        path('traitement/', views.traitement),
        path('traitement2/', views.traitement2),
        path('', views.home),
        path('affichage/', views.affichage),
        path('affichage2/', views.affichage2),

        path('affiche/<int:id>/', views.affiche),
        path('affiche2/<int:id>/', views.affiche2),

        path('update/<int:id>/', views.update),
        path('updatetraitement/<int:id>/', views.updatetraitement),

        path('update2/<int:id>/', views.update2),
        path('updatetraitement2/<int:id>/', views.updatetraitement2),

        path('delete/<int:id>/', views.delete),
        path('delete2/<int:id>/', views.delete2),
]