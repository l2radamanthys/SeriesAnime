#!/usr/bin/env python
# -*- coding: utf-8 -*-


from django import forms
from django.forms import TextInput, NumberInput, Select, Textarea, FileInput
from Main.models import *



class SerieForm(forms.ModelForm):
    class Meta:
        model = Serie
        exclude = {
            'id'
        }
        widgets = {
            'name' : TextInput(attrs={'class': 'form-control'}),
            'chapters' : TextInput(attrs={'class': 'form-control'}),
            'descripcion' : Textarea(attrs={'class': 'form-control' , 'rows':'3'}),
            'gender' : TextInput(attrs={'class': 'form-control'}),
            'status' : Select(attrs={'class': 'form-control'}),
            'rank' : Select(attrs={'class': 'form-control'}),
            'image': FileInput(attrs={'class': 'form-control', 'placeholder': 'seleccione una imagen'}),
            'code' : TextInput(attrs={'class': 'form-control'}),
            'in_disk' : Select(attrs={'class': 'form-control'}),
            'complete' : Select(attrs={'class': 'form-control'}),
            'ubication' : TextInput(attrs={'class': 'form-control'}),
            'observations' : Textarea(attrs={'class': 'form-control' , 'rows':'3'}),
        }



class ServerForm(forms.ModelForm):
    class Meta:
        model = Server
        exclude = {
            'id',
            'serie',
        }
        widgets = {
            'name' : TextInput(attrs={'class': 'form-control'}),
            'url' : TextInput(attrs={'class': 'form-control'}),
            'url_format' : TextInput(attrs={'class': 'form-control'}),
        }