# Generated by Django 4.0.4 on 2022-05-27 16:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Master', '0015_alter_paymodel_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='paymodel',
            old_name='user',
            new_name='us',
        ),
    ]
