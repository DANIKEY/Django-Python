from django.conf.urls import url

from . import views

urlpatterns = [

    url(r'^$', views.connexion, name='connexion'),
    url(r'^enregistreProcedure$', views.enregistreProcedure, name='enregistreProcedure'),
    url(r'^listeProcedures$', views.listeProcedures, name='listeProcedures'),
    url(r'^statistiques$', views.statistiques, name='statistiques'),
    url(r'^selectionnerProcedure$', views.selectionnerProcedure, name='selectionnerProcedure'),
    url(r'^supprimerProcedure/(?P<id>\d+)/(?P<page>\d+)$', views.supprimerProcedure, name='supprimerProcedure'),
    url(r'^afficheProcedureId/(?P<id>\d+)$', views.afficheProcedureId, name='afficheProcedureId'),
    url(r'^updateProcedure/(?P<idProcedure>\d+)$', views.updateProcedure, name='updateProcedure'),    
    url(r'^deconnexion$', views.deconnexion, name='deconnexion'),
]

