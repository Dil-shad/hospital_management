# Generated by Django 4.0.4 on 2022-05-24 14:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Master', '0004_docter_dep_remove_doctormodel_department_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='doctormodel',
            old_name='profile_pic',
            new_name='image',
        ),
    ]