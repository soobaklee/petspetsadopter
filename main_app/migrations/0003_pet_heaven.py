# Generated by Django 2.1.5 on 2019-03-14 03:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_energy'),
    ]

    operations = [
        migrations.AddField(
            model_name='pet',
            name='heaven',
            field=models.BooleanField(default=False),
        ),
    ]
