# Generated by Django 3.2.15 on 2022-09-25 05:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('family_budget', '0010_auto_20220924_2057'),
    ]

    operations = [
        migrations.AddField(
            model_name='budget',
            name='added',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now, verbose_name='Added ad'),
        ),
        migrations.AlterField(
            model_name='budget',
            name='slug',
            field=models.SlugField(blank=True, default='7159334ce6cb4433acd9ca682a73f27a', max_length=150, null=True, unique=True, verbose_name='Link'),
        ),
        migrations.AlterField(
            model_name='budgetitems',
            name='added',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Added at'),
        ),
    ]
