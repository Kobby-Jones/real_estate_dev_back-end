from django.db import models

class Agent(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField()
    image = models.ImageField()
    

    def __init__(self):
        return self.username

