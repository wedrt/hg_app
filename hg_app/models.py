from django.db import models
from json import dumps, loads
from django.contrib.auth.models import User


class Package(models.Model):
    id = models.AutoField(primary_key=True)
    long = models.DecimalField(max_digits=9, decimal_places=6)
    lat = models.DecimalField(max_digits=9, decimal_places=6)
    description = models.CharField(max_length=100)
    opening_time = models.DateTimeField()
    picked_up = models.BooleanField()


class Point(models.Model):
    id = models.AutoField(primary_key=True)
    long = models.DecimalField(max_digits=9, decimal_places=6)
    lat = models.DecimalField(max_digits=9, decimal_places=6)
    description = models.CharField(max_length=100)
    opening_time = models.DateTimeField()
    codes = models.CharField(max_length=200)

    # using json to store the codes
    def set_codes(self, x):
        self.set_codes = dumps(x)

    def get_codes(self):
        return loads(self.codes)


class Message(models.Model):
    text = models.CharField(max_length=300)
    brief = models.CharField(max_length=20)
    time = models.TimeField(auto_now=True)

    def __str__(self):
        return self.brief





class Player(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    lives = models.IntegerField()

    def __str__(self):
        return self.user.username


class Kill(models.Model):
    killer = models.ManyToManyField(Player)
    victim = models.ManyToManyField(Player)
    stealth_kill = models.BooleanField()
    time = models.TimeField(auto_now=True)



