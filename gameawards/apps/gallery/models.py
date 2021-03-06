from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Img(models.Model):
    title = models.CharField(max_length = 100)
    image = models.ImageField(upload_to="images")
    added_date = models.DateField(default=timezone.now())
    owner = models.ForeignKey(User)
    
    def __unicode__(self):
        return self.title
    
class ProfilePic(models.Model):
    title = models.CharField(max_length = 100)
    image = models.ImageField(upload_to="images/profiles")
    added_date = models.DateField(default=timezone.now())
    owner = models.ForeignKey(User)
    
    def __unicode__(self):
        return self.title

class GamePic(models.Model):
    title = models.CharField(max_length = 100)
    image = models.ImageField(upload_to="images/games")
    added_date = models.DateField(default=timezone.now())
    owner = models.ForeignKey(User)
    game = models.ForeignKey('runs.Game')
    game_icon = models.BooleanField(default=False)
    
    def __unicode__(self):
        return self.title
        
class AdminPic(models.Model):
    title = models.CharField(max_length = 100)
    added_date = models.DateField(default=timezone.now())
    image = models.ImageField(upload_to="images/admin")
    
    
    
    
    
    
