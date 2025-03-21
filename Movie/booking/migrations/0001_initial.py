# Generated by Django 3.0.3 on 2020-04-25 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Seat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30)),
                ('moviename', models.CharField(max_length=30)),
                ('date', models.IntegerField()),
                ('row', models.CharField(max_length=10)),
                ('column', models.CharField(max_length=10)),
                ('time', models.IntegerField()),
            ],
            options={
                'unique_together': {('moviename', 'date', 'row', 'column', 'time')},
            },
        ),
    ]
