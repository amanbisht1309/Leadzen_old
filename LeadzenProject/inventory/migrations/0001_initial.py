# Generated by Django 4.0.1 on 2022-02-08 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('phone_number', models.CharField(max_length=12, unique=True)),
                ('email', models.CharField(max_length=250, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Rentals',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(max_length=500)),
                ('rental_date', models.DateField()),
                ('return_date', models.DateField()),
                ('vehicle_type', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='vehicle_type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vehicle_name', models.CharField(max_length=250)),
                ('tot_availabile', models.IntegerField()),
            ],
        ),
    ]
