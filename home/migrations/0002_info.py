# Generated by Django 3.2.6 on 2021-08-07 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=300)),
                ('local_address', models.CharField(max_length=300)),
                ('phone', models.CharField(max_length=200)),
                ('time', models.CharField(max_length=300)),
                ('email', models.CharField(max_length=200)),
            ],
        ),
    ]
