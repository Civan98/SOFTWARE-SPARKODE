# Generated by Django 3.0 on 2020-01-03 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pnl', '0004_auto_20200103_1438'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ejercicio',
            name='IdTem',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
