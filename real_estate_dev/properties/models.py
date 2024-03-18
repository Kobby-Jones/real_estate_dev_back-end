from django.db import models

class Properties(models.Model):
    TYPE_CHOICES = [
        ('Condo', 'Condo'),
        ('TownHouse', 'TownHouse'),
        ('Apartment', 'Apartment'),
        ('House', 'House'),
        ('Modular Home', 'Modular Home'),
        ('Single-Family House', 'Single-Family House'),
    ]
    type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    image = models.ImageField()
    bedRooms = models.PositiveIntegerField()
    bathRooms = models.PositiveIntegerField()
    address = models.CharField(max_length=255)
    agent = models.ForeignKey(Agent, on_delete=models.CASCADE)
    is_for_rent = models.BooleanField(default=True)  # True if the property is for rent, False if it's for sale
    description = models.TextField()

    def __str__(self):
        return f"{self.type} - {self.address}"
    

