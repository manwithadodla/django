from django.contrib import admin
from .models import Participant, Dataset, Phenotype, Scan, Protocol, Site, Session

admin.site.register(Participant)
admin.site.register(Dataset)
admin.site.register(Phenotype)
admin.site.register(Scan)
admin.site.register(Protocol)
admin.site.register(Site)
admin.site.register(Session)