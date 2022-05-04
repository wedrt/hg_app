# Generated by Django 4.0.4 on 2022-04-29 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hg_app', '0013_alter_message_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='package',
            name='lat',
            field=models.DecimalField(decimal_places=6, max_digits=9, verbose_name='latitude (N)'),
        ),
        migrations.AlterField(
            model_name='package',
            name='long',
            field=models.DecimalField(decimal_places=6, max_digits=9, verbose_name='longitude (E)'),
        ),
        migrations.AlterField(
            model_name='point',
            name='lat',
            field=models.DecimalField(decimal_places=6, max_digits=9, verbose_name='latitude (N)'),
        ),
        migrations.AlterField(
            model_name='point',
            name='long',
            field=models.DecimalField(decimal_places=6, max_digits=9, verbose_name='longitude (E)'),
        ),
    ]
