# Generated by Django 3.0.2 on 2020-05-10 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_auto_20200510_1652'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='name',
            field=models.CharField(default='', max_length=30),
        ),
    ]