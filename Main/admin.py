
from django.contrib import admin
from Main.models import *


class ModelAdmin(admin.ModelAdmin):
    pass


admin.site.register(Serie, ModelAdmin)
admin.site.register(RelacionSeries, ModelAdmin)
admin.site.register(Server, ModelAdmin)