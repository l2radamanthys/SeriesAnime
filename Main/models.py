#!/usr/bin/env python
# -*- coding: utf-8 -*-


from django.db import models
from SeriesAnime.my_setings import *



class Serie(models.Model):
    """
        Series
    """
    name = models.CharField("Nombre", max_length=100)
    code = models.CharField("Codigo", max_length=50)
    descripcion = models.TextField("Descripcion")
    rank = models.TextField("Calificacion", max_length="1", choices=RANK_CHOICES, default="2")
    image = models.ImageField("Portada", upload_to="media/uploads")
    chapters = models.IntegerField("Numero de Capitulos")
    status = models.CharField("Estado", max_length=1, choices=STATUS_CHOICES)
    gender = models.CharField("Genero", max_length=150)
    in_disk = models.BooleanField("Almacena Localmente", choices=SI_NO_CHOICES, default=False)
    complete = models.BooleanField("Completa", choices=SI_NO_CHOICES, default=False)
    ubication = models.CharField("Ubicacion", max_length=255, default="/")
    observations = models.TextField("Observaciones", default="")


    class Meta:
        db_table = "Series"
        verbose_name = "Serie"
        verbose_name_plural = "Series"
        ordering = ['-id']


    def servers(self):
        return Server.objects.filter(serie=self)


    def __unicode__(self):
        return self.name



class Server(models.Model):
    """
        Servidores
    """
    name = models.CharField("Nombre", max_length=100)
    url = models.CharField("url", max_length=150, default="http://")
    url_format = models.CharField("formato", max_length=150, default="http://")
    serie = models.ForeignKey(Serie)


    class Meta:
        db_table = "Servidores"
        verbose_name = "Servidor"
        verbose_name_plural = "Servidores"


    def get_chapter_url(self, number):
        return self.url_format.format(number)


    def __unicode__(self):
        return self.name