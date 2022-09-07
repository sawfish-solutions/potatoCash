# Generated by Django 4.0.6 on 2022-09-07 05:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expenses', '0004_remove_expenses_exp_value_expenses_expvalue'),
    ]

    operations = [
        migrations.AddField(
            model_name='expenses',
            name='expcategory',
            field=models.CharField(default='test_cat', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='expenses',
            name='firstname',
            field=models.CharField(default='test_fn', max_length=255),
        ),
        migrations.AddField(
            model_name='expenses',
            name='lastname',
            field=models.CharField(default='test_sn', max_length=255),
        ),
        migrations.AddField(
            model_name='expenses',
            name='username',
            field=models.CharField(default='test', max_length=255),
        ),
        migrations.AlterField(
            model_name='expenses',
            name='expvalue',
            field=models.IntegerField(),
        ),
    ]
