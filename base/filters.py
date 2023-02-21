import django_filters

from .models import *

class studentResult(django_filters.FilterSet):
   class Meta:
       model = Science
       fields = ['StudentNo', 'TERM', 'YEAR']