# Generated by Django 4.0.4 on 2022-05-27 17:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Master', '0020_remove_paymodel_user_paymodel_doc_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='paymodel',
            old_name='doc_id',
            new_name='doc',
        ),
    ]
