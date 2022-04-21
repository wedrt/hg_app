from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from hg_app.models import Player, Kill


@receiver(post_save, sender=User)
def create_player(instance, created, **kwargs):
    if created:
        Player.objects.create(
            user=instance
        )


@receiver(post_save, sender=Kill)
def remove_live(instance, created, **kwargs):
    if created:
        victim = instance.victim
        victim.lives -= 1
        victim.save()
