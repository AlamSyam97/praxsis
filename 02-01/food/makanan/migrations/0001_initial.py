# Generated by Django 3.2.8 on 2021-10-14 03:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='makanan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jenis', models.CharField(default='', max_length=10)),
                ('nama', models.CharField(default='', max_length=15)),
                ('harga', models.IntegerField()),
            ],
        ),
    ]
