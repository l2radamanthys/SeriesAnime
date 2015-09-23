from django.db import models
from my_setings import *



class Serie(models.Model):
    """
        Series
    """
    name = models.CharField("Nombre", max_lenght=100)
    image = models.ImageField("Portada", upload_to="media/uploads")
    chapters = models.IntegerField("Numero de Capitulos")
    status = models.CharField("Estado", max_lenght=1, choices=STATUS_CHOICES)


    class Meta:
        db_table = "Series"
        verbose_name = "Serie"
        verbose_name_plural = "Series"


    def __unicode__(self):
        return self.name



class Server(models.Model):
    """
        Servidores
    """
    name = models.CharField("Nombre", max_lenght=100)
    url = models.CharField("url", max_lenght=150)
    url_format = models.CharField("formato", max_lenght=150)
    serie = models.ForeignKey(Serie)


    class Meta:
        db_table = "Servidores"
        verbose_name = "Servidor"
        verbose_name_plural = "Servidores"


    def get_chapter_url(self, number):
        return self.url_format.format(number)


    def __unicode__(self):
        return self.name