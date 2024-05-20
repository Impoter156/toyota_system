# Generated by Django 5.0.6 on 2024-05-20 03:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('phone_number', models.IntegerField(default=0)),
                ('position', models.CharField(choices=[('Sell', 'Sell'), ('Manager', 'Manager'), ('Accountant', 'Accountant'), ('Team-Leader', 'Team-Leader')], default='', max_length=255)),
                ('working_days', models.IntegerField(blank=True, default=0, null=True)),
                ('day_off', models.IntegerField(blank=True, default=0, null=True)),
            ],
        ),
    ]
