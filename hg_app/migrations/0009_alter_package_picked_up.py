# Generated by Django 4.0.3 on 2022-04-24 18:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hg_app', '0008_alter_kill_murderer_alter_kill_stealth_kill_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='package',
            name='picked_up',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hg_app.player'),
        ),
    ]