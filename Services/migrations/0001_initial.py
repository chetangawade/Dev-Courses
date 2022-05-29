# Generated by Django 4.0.3 on 2022-05-20 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='cloud_computing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language', models.CharField(max_length=50)),
                ('language_info', models.CharField(max_length=200)),
                ('reference_link', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='machine_learning',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language', models.CharField(max_length=50)),
                ('language_info', models.CharField(max_length=200)),
                ('reference_link', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='software_testing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language', models.CharField(max_length=50)),
                ('language_info', models.CharField(max_length=200)),
                ('reference_link', models.CharField(max_length=100)),
            ],
        ),
    ]