# Generated by Django 4.0.6 on 2022-09-07 00:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Expenses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exp_value', models.CharField(max_length=50)),
            ],
        ),
    ]
