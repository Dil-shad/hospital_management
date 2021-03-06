# Generated by Django 4.0.4 on 2022-05-24 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Master', '0003_remove_doctormodel_emp_address_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Docter_dep',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department', models.CharField(max_length=50)),
            ],
        ),
        migrations.RemoveField(
            model_name='doctormodel',
            name='department',
        ),
        migrations.AlterField(
            model_name='doctormodel',
            name='status',
            field=models.BooleanField(default=True),
        ),
    ]
