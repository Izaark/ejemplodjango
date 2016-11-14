from __future__ import unicode_literals

from django.db import models


class Habitantes(models.Model):
	#Attributes
	species = models.CharField(max_length=15, null=False, blank=False)
	number = models.IntegerField(blank=False, null=True, default=0)
	smart = models.BooleanField(default=False)


  	def __str__(self):
  		return "Los {0}".format(self.species)
  				#"La especie {0} tiene {1}".format(self.species, str(self.number))
class Galaxia(models.Model):
	#Attributes
	name = models.CharField(max_length=15, blank=False, null=False)
	diameter = models.IntegerField(blank=False, null=True, default=0)
	distance = models.IntegerField(blank=False, null=True, default=0)
	def __str__(self):
		return "esta en la galaxia {0} tiene {1} de diametro".format(self.name, str(self.diameter))
    
class Planeta(models.Model):

    class Meta:
        verbose_name = "Planeta"
        verbose_name_plural = "Planetas"
    #Atributes
    name = models.CharField(max_length=20, blank=False,null=False)
    number_moons = models.IntegerField(blank=False, null=True, default=0)
    color = models.CharField(max_length=10, blank=False,null=False)
    volume = models.IntegerField(blank=True,null=True)
    era = models.CharField(max_length=10,blank=True,null=False)
    habitable = models.BooleanField(default=False)
    #Relations
    especie = models.ForeignKey(Habitantes, related_name='planeta_especie')
    galaxia = models.ForeignKey(Galaxia, related_name='planeta_galaxia')


    def __str__(self):
        return self.name
    
    
