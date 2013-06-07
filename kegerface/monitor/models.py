from django.db import models

LEVELS = ((0, '0%'), (10, '10%'), (25, '25%'), (50, '50%'), (75, '75%'), (100, '100%'))
SRMS = ((1, '1'), (5, '5'), (10, '10'), (15, '15'), (20, '20'), (25, '25'), (30, '30'), (36, '36'), (40, '40'))

class Tap(models.Model):
    tap_number = models.IntegerField(primary_key=True)
    level = models.IntegerField(choices=LEVELS, blank=True, null=True)
    beer = models.ForeignKey('Beer', blank=True, null=True)
    
    def __unicode__(self):
        return "{} - {}".format(self.tap_number, self.beer)
    
    def level_image(self):
        if self.level:
            return 'images/kegs/{}.png'.format(self.level)
        return 'images/kegs/0.png'


class Beer(models.Model):
    name = models.CharField(max_length=100)
    style = models.CharField(max_length=50, blank=True, null=True)
    brewery = models.CharField(max_length=50, blank=True, null=True)
    abv = models.FloatField(blank=True, null=True)
    ibu = models.IntegerField(blank=True, null=True)
    srm = models.IntegerField(choices=SRMS, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    
    def __unicode__(self):
        return self.name
    
    def srm_image(self):
        if self.srm:
            return 'images/SRM {}.png'.format(self.srm)
        return 'images/blank.png'
    
    def hops_image(self):
        if self.ibu:
            hops = min(self.ibu // 25, 3) 
            return 'images/{} Hops.png'.format(hops)
        return 'images/0 Hops.png'
