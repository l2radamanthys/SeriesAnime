#!/usr/bin/env python
# -*- coding: utf-8 -*-


from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, Context
from django.template.loader import get_template
from django.contrib.auth.models import User
from django.contrib import auth

from Main.models import *
from Main.myforms import *



def home(request):
    template = get_template('home.html')
    data = {}
    data['series'] = Serie.objects.filter(status='A').order_by('name')
    view_cont = template.render(data)
    return HttpResponse(view_cont)



def all_serie(request):
    template = get_template('series-todas.html')
    data = {}
    data['series'] = Serie.objects.filter()
    view_cont = template.render(data)
    return HttpResponse(view_cont)



def add_serie(request):
    template = get_template('series-agregar.html')
    data = {}
    if request.method == 'POST':
        form = SerieForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/series/')
        else:
            data['form'] = form

    else:
        default_data = {
            'code': 0,
            'gender': 'sin especificar',
            'status': 'F',
            'descripcion': 'sin descripción',
            'chapters': '0',
            'observations': 'sin observaciones',
        }
        data['form'] = SerieForm(initial=default_data)

    view_cont = template.render(data)
    return HttpResponse(view_cont)



#this a clon of add serie only changed template
def rapid_add_serie(request):
    template = get_template('series-agregar-simple.html')
    data = {}
    if request.method == 'POST':
        default_data = {
            'descripcion': 'sin descripción',
            'observations': 'sin observaciones',
            'ubication': '/',
        }
        request.POST.update(default_data)

        form = SerieForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
        else:
            data['form'] = form
            print(form.errors)

    else:
        default_data = {
            'code': 0,
            'gender': 'sin especificar',
            'status': 'A',
            'descripcion': 'sin descripción',
            'chapters': '0',
            'observations': 'sin observaciones',
            'ubication': '/',
        }
        data['form'] = SerieForm(initial=default_data)

    view_cont = template.render(data)
    return HttpResponse(view_cont)



def edit_serie(request, id_):
    template = get_template('series-agregar.html')
    serie = Serie.objects.get(id=id_)
    data = {}
    if request.method == 'POST':
        form = SerieForm(request.POST, request.FILES, instance=serie)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/series/')

        else:
            data['form'] = form

    else:
        data['form'] = SerieForm(instance=serie)

    view_cont = template.render(data)
    return HttpResponse(view_cont)



def delete_serie(request, id_):
    try:
        serie = Serie.objects.get(id=id_)
        serie.delete()
        return HttpResponseRedirect('/')
    except:
        return HttpResponseRedirect('/')



def show_serie(request, id_):
    template = get_template('series-mostrar.html')
    data = {}
    data['serie'] = Serie.objects.get(id=id_)
    view_cont = template.render(data)
    return HttpResponse(view_cont)



def search_serie(request):
    template = get_template('buscar.html')
    data = {}
    data['series'] = Serie.objects.filter()
    view_cont = template.render(data)
    return HttpResponse(view_cont)



def add_server_serie(request, id_):
    template = get_template('series-agregar-servidor.html')
    serie_ = Serie.objects.get(id=id_)
    data = {}
    data['serie'] = serie_
    if request.method == 'POST':
        form = ServerForm(request.POST)
        if form.is_valid():
            server = Server(
                serie = serie_,
                name = form.cleaned_data['name'],
                url = form.cleaned_data['url'],
                url_format = form.cleaned_data['url_format'],
            )
            server.save()
            return HttpResponseRedirect('/')
        else:
            data['form'] = form

    else:
        data['form'] = ServerForm()

    view_cont = template.render(data)
    return HttpResponse(view_cont)


