# Generated by Django 3.0.5 on 2020-05-31 22:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20200531_2218'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='photo',
            field=models.BooleanField(default=False),
        ),
    ]
