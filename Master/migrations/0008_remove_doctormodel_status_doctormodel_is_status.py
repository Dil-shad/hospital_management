# Generated by Django 4.0.4 on 2022-05-25 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Master', '0007_patientmodel'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='doctormodel',
            name='status',
        ),
        migrations.AddField(
            model_name='doctormodel',
            name='is_status',
            field=models.BooleanField(default=False),
        ),
    ]
