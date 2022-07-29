# Generated by Django 4.0.6 on 2022-07-21 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ApplicationRandomModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_open', models.DateField()),
                ('date_close', models.DateField()),
                ('result', models.TextField(null=True)),
                ('generated_amount', models.PositiveIntegerField()),
            ],
        ),
    ]
