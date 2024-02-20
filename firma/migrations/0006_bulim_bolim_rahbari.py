# Generated by Django 5.0.2 on 2024-02-19 08:48

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firma', '0005_remove_bulim_bolim_rahbari'),
    ]

    operations = [
        migrations.AddField(
            model_name='bulim',
            name='bolim_rahbari',
            field=models.OneToOneField(default=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
