# Generated by Django 4.0.6 on 2022-07-23 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WebSite', '0002_applicationrandommodel_unique_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='applicationrandommodel',
            name='_range',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
