from import_export import resources
from .models import *

class SightingResource(resources.ModelResource):
    class Meta:
        model = Sightings
       	exclude = ('id',)
       	import_id_fields = ('NAME','PERSON','LOCATION','SIGHTED')

class FlowerResource(resources.ModelResource):
    class Meta:
        model = Flowers

class FeaturesResource(resources.ModelResource):
    class Meta:
        model = Features