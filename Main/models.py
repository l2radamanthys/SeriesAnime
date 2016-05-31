#!/usr/bin/env python
# -*- coding: utf-8 -*-


from django.db import models
from SeriesAnime.my_settings import *



class Serie(models.Model):
    """
        Series
    """
    name = models.CharField("Nombre", max_length=100)
    code = models.CharField("Codigo", max_length=50)
    descripcion = models.TextField("Descripcion")
    #year = models.CharField(u"Año", max_length=4)
    rank = models.TextField("Calificacion", max_length="1", choices=RANK_CHOICES, default="2")
    image = models.ImageField("Portada", upload_to="media/uploads", default='media/uploads/default_image.png')
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
        ordering = ['code', 'name', '-id']


    def empty_image(self):
        print(self.image);
        return false;


    def rank_to_stars(self):
        t_star = '<i class="fa fa-star gold"></i>'
        f_star = '<i class="fa fa-star gray"></i>'
        return t_star * int(self.rank) + (f_star * (5 - int(self.rank)))


    def servers(self):
        return Server.objects.filter(serie=self)


    def not_servers(self):
        return len(Server.objects.filter(serie=self))

    def __unicode__(self):
        return u"{} - {}".format(self.code, self.name)


    def __str__(self):
        return self.__unicode__()



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
        ordering = ['name']


    def get_chapter_url(self, number):
        return self.url_format.format(number)


    def __unicode__(self):
        return self.name


    def __str__(self):
        return self.__unicode__()



class RelacionSeries(models.Model):
    serie_a = models.ForeignKey(Serie, related_name='serie_a')
    serie_b = models.ForeignKey(Serie, related_name='serie_b')
    relation = models.CharField(max_length=1, choices=RELACION_SERIES_CHOICES, default="N")

    class Meta:
        db_table = "SeriesRelacion"
        verbose_name = "Series Relacion"
        verbose_name_plural = "Series Relaciones"
        ordering = ['id']


    def __unicode__(self):
        return "{} - {}".format(self.serie_a, self.serie_b)


    def __str__(self):
        return self.__unicode__()
