# Generated by Django 4.0.4 on 2023-03-19 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_alter_appointment_rest_data_desc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment_rest_data',
            name='desc',
            field=models.CharField(default='No', max_length=200),
        ),
    ]
