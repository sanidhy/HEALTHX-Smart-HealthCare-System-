# Generated by Django 4.0.4 on 2023-03-19 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_patient_appointment_mail'),
    ]

    operations = [
        migrations.CreateModel(
            name='appointment_rest_data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hospital', models.CharField(max_length=20)),
                ('date', models.CharField(max_length=10)),
                ('Time', models.CharField(max_length=30)),
                ('desc', models.CharField(max_length=200)),
            ],
        ),
    ]