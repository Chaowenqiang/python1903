# Generated by Django 2.2.2 on 2019-06-17 01:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20190613_1540'),
    ]

    operations = [
        migrations.CreateModel(
            name='Img',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pic', models.ImageField(upload_to='static/media/')),
                ('desc', models.CharField(max_length=100)),
                ('url', models.CharField(max_length=100)),
            ],
        ),
    ]
