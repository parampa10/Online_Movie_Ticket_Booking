# Generated by Django 3.0.3 on 2020-03-14 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieupdate', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='movieimg',
            field=models.ImageField(height_field=250, upload_to='images/', width_field=168),
        ),
    ]
