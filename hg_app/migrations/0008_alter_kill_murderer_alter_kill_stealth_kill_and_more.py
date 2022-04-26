# Generated by Django 4.0.3 on 2022-04-20 18:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('hg_app', '0007_remove_player_kills_kill_murderer_alter_kill_victim_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kill',
            name='murderer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='my_kills', to='hg_app.player'),
        ),
        migrations.AlterField(
            model_name='kill',
            name='stealth_kill',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='kill',
            name='victim',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='my_deaths', to='hg_app.player'),
        ),
        migrations.AlterField(
            model_name='player',
            name='lives',
            field=models.IntegerField(default=3),
        ),
        migrations.AlterField(
            model_name='player',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='player', to=settings.AUTH_USER_MODEL),
        ),
    ]