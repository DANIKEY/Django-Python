# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render , redirect
from django.http import HttpResponse, Http404
from django.http import HttpResponseRedirect
from .form_login import FormAuthentification
from .formEnregistreProcedure import EnregistreForm
from .formSelect import FormSelect
from  applicationWestaflex.models import EnregistreProcedure,Statistiques,ProcedureSelectionnee
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.core.urlresolvers import reverse

def connexion(request):
    error = False
    if request.method == "POST":
       form = FormAuthentification(request.POST)
    
       if form.is_valid():
          username = form.cleaned_data['utilisateur']
          password = form.cleaned_data['mot_passe']
          user  = authenticate(username=username,password=password)
          
          if user:
              login(request, user)
          else:
               error = True
      
    else:
        form = FormAuthentification()
            
    return render(request,'applicationWestaflex/login.html',locals())

def deconnexion(request):
    logout(request)
    return redirect(reverse(connexion))

def enregistreProcedure(request):
    form = EnregistreForm(request.POST or None)
    if form.is_valid():
    
            client = form.cleaned_data['client']
            pression = form.cleaned_data['pression']
            duree = form.cleaned_data['duree']
            marge = form.cleaned_data['marge']
            diametre = form.cleaned_data['diametre']
            reference = form.cleaned_data['reference']
            EnregistreProcedure(client=client,pression=pression,duree=duree,marge=marge,diametre=diametre,reference=reference).save()
            
            envoi = True 

    return render(request,'applicationWestaflex/EnregistreProcedure.html',locals())

def listeProcedures(request):
    
    procedure = EnregistreProcedure.objects.all()
    return render(request,'applicationWestaflex/ListeProcedures.html',{'procedures':procedure})   

def statistiques(request):
    
    stats = Statistiques.objects.all()
    return render(request,'applicationWestaflex/Stats.html',{'stats':stats})        

def selectionnerProcedure(request):
    
    procedure = EnregistreProcedure.objects.all()
    return render(request,'applicationWestaflex/SelectionProcedure.html',{'procedures':procedure})     

def supprimerProcedure(request,id,page):
    
    procedure = EnregistreProcedure.objects.get(id_procedure=id)
    procedure.delete()
    argument = page.split("/")
    lien = argument[0]
    
    if lien == "1" :
        return redirect(listeProcedures)
    elif lien == "2" :
        return redirect(selectionnerProcedure)    

def afficheProcedureId(request,id):
    
    procedure = EnregistreProcedure.objects.get(id_procedure=id)
    return render(request, 'applicationWestaflex/afficheProcedureId.html', {'procedure': procedure})

def updateProcedure(request,idProcedure):
    
    requete  = ProcedureSelectionnee.objects.get(id=1)
    requete.id_procedure = idProcedure
    requete.save() 
    return redirect(selectionnerProcedure)
    
    

