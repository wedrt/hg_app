from django.db import models
from json import dumps, loads
from django.contrib.auth.models import User


class Package(models.Model):
    long = models.DecimalField(max_digits=9, decimal_places=6)
    lat = models.DecimalField(max_digits=9, decimal_places=6)
    description = models.CharField(max_length=100)
    opening_time = models.DateTimeField()
    picked_up = models.BooleanField()


class Point(models.Model):
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


class Kill(models.Model):
    victim = models.ForeignKey('Player', on_delete=models.CASCADE, related_name='my_deaths')
    murderer = models.ForeignKey('Player', on_delete=models.CASCADE, related_name='my_kills')
    stealth_kill = models.BooleanField(default=False)
    time = models.TimeField(auto_now=True)

    def __str__(self):
        return f"{self.victim} was killed by {self.murderer}"


class Player(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='player')
    lives = models.IntegerField(default=3)
    points = models.ManyToManyField(Point, blank=True)
    packages = models.ManyToManyField(Package, blank=True)
    messages = models.ManyToManyField(Message, blank=True)
    # photo = models.ImageField(upload_to='photos')

    def __str__(self):
        return self.user.username

    # def lives(self):
    #     return 3 - self.my_deaths.count()




