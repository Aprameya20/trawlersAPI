# Generated by Django 3.1.5 on 2021-02-01 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ship',
            fields=[
                ('mmsi', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('date', models.DateField(auto_now=True)),
                ('flag', models.CharField(max_length=100)),
                ('eez_crossing', models.CharField(max_length=100)),
                ('violation', models.CharField(max_length=100)),
            ],
        ),
    ]
