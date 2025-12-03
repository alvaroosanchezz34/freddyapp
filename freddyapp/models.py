from django.db import models

# Model for parties that animatronics can attend
class Party(models.Model):
    """Modelo que representa una fiesta con nombre y cantidad de asistentes"""
    name = models.CharField(max_length=100)
    attendants = models.IntegerField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Parties"


# Main model for animatronics
class Animatronic(models.Model):
    """Modelo que representa un animatrónico con sus propiedades"""
    
    # Animal type choices for the animatronic
    ANIMAL_CHOICES = [
        ('BE', 'Bear'),
        ('CH', 'Chicken'),
        ('BU', 'Bunny'),
        ('FO', 'Fox'),
    ]
    
    name = models.CharField(max_length=50)
    animal = models.CharField(max_length=2, choices=ANIMAL_CHOICES)
    build_date = models.DateField()
    decommissioned = models.BooleanField(default=False)
    # ManyToMany relationship with Party
    parties = models.ManyToManyField(Party, blank=True)

    def __str__(self):
        return self.name
