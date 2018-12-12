from import_export import resources
from models import *

class SightingResource(resources.ModelResource):
	class Meta:
		model = Sightings

class FlowerResource(resources.ModelResource):
    class Meta:
        model = Flowers

class FeaturesResource(resources.ModelResource):
    class Meta:
        model = Features