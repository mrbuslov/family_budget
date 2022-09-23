# Generated by Django 3.2.15 on 2022-09-22 16:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Budget',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=2000, unique=True, verbose_name='Name')),
                ('slug', models.SlugField(blank=True, default='2eca986c05d14d9c9d3e0ff3be33088f', max_length=150, null=True, unique=True, verbose_name='Link')),
                ('description', models.TextField(blank=True, max_length=5500, null=True, verbose_name='Description')),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Owner')),
            ],
            options={
                'verbose_name': 'Budget',
                'verbose_name_plural': 'Budgets',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True, verbose_name='Name')),
                ('budget', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='family_budget.budget', verbose_name='Budget')),
            ],
        ),
        migrations.CreateModel(
            name='BudgetItems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=2000, null=True, verbose_name='Name')),
                ('price', models.DecimalField(decimal_places=2, max_digits=20, verbose_name='Price')),
                ('description', models.TextField(blank=True, max_length=5500, null=True, verbose_name='Description')),
                ('added', models.DateTimeField(auto_now_add=True, verbose_name='Added ad')),
                ('currency', models.CharField(choices=[('usd', 'Dollar'), ('euro', 'Euro')], default='usd', max_length=20)),
                ('budget', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='family_budget.budget', verbose_name='Budget')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='family_budget.category', verbose_name='Category')),
            ],
        ),
    ]