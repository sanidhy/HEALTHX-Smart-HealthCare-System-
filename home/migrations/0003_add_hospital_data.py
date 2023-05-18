# Generated by Django 4.0.4 on 2023-03-02 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_rename_addres_patient_appointment_address_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='add_hospital_data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('mail', models.CharField(max_length=30)),
                ('phone', models.CharField(max_length=10)),
                ('capaity', models.CharField(max_length=10)),
                ('oxygen', models.CharField(max_length=10)),
                ('beds', models.CharField(max_length=10)),
                ('city', models.CharField(max_length=30)),
                ('dept', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=100)),
            ],
        ),
    ]
