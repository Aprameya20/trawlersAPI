# Generated by Django 3.1.6 on 2021-02-02 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('APIapp', '0004_ais'),
    ]

    operations = [
        migrations.CreateModel(
            name='FilesAdmin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('upload', models.FileField(upload_to='media')),
                ('title', models.CharField(max_length=50)),
            ],
        ),
    ]
