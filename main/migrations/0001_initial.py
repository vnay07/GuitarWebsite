# Generated by Django 3.0.2 on 2020-05-07 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=50)),
                ('category', models.CharField(max_length=50)),
                ('subCategory', models.CharField(max_length=50)),
                ('image', models.ImageField(default='default.png', upload_to='guitar/images')),
            ],
        ),
    ]
