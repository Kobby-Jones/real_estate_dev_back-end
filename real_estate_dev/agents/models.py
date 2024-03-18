from django.db import models

class Agent(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=50)
    image = models.ImageField()
    

    def __str__(self):
        return self.username

