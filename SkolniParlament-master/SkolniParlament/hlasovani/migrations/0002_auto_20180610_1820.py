# Generated by Django 2.0.6 on 2018-06-10 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hlasovani', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datafile',
            name='data',
            field=models.FileField(upload_to='uploaded_files'),
        ),
    ]
