# Generated by Django 4.0.4 on 2022-05-27 16:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Master', '0016_rename_user_paymodel_us'),
    ]

    operations = [
        migrations.RenameField(
            model_name='paymodel',
            old_name='us',
            new_name='user',
        ),
    ]
