# Generated by Django 2.0.6 on 2019-04-28 01:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('placarPPR', '0003_auto_20190427_2240'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='farol',
            field=models.TextField(max_length=20),
        ),
        migrations.AlterField(
            model_name='post',
            name='percent_ating',
            field=models.DecimalField(decimal_places=2, max_digits=2),
        ),
    ]
