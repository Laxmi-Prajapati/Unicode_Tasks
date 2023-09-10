from django.db import models

# Create your models here.
class PokemonCaught(models.Model):
    name = models.CharField(max_length=100)
    level = models.IntegerField(default=1)
    sprites = models.URLField(default = "https://www.generalservicesonline.com/images/Datanotavailable.gif")
    height = models.FloatField(blank=True, null=True)
    moves = models.JSONField(blank=True, null=True)
    

    def __str__(self):
        return self.name
    
