# Generated by Django 3.0.5 on 2020-04-19 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='status',
            field=models.CharField(choices=[(0, 'no action'), (1, 'video selected by owner'), (2, 'check validation'), (3, 'video played by owner')], max_length=32),
        ),
    ]
