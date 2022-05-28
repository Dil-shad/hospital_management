# Generated by Django 4.0.4 on 2022-05-27 13:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Master', '0012_appoinmentmodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='appoinmentmodel',
            name='date',
            field=models.CharField(default=12, max_length=15),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='docter_dep',
            name='department',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.CreateModel(
            name='PayModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fees', models.CharField(blank=True, max_length=20, null=True)),
                ('salary', models.CharField(blank=True, max_length=20, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]