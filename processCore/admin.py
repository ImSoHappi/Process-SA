from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Client)
admin.site.register(UnidadInterna)
admin.site.register(Process)
admin.site.register(Task)
admin.site.register(TareaSubordinada)
admin.site.register(FlujoTareas)
admin.site.register(Rejectcomment)
admin.site.register(ProblemaTarea)