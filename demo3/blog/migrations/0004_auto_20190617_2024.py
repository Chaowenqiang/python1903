# Generated by Django 2.2.2 on 2019-06-17 12:24

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_img'),
    ]

    operations = [
        migrations.CreateModel(
            name='MessageInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('content', tinymce.models.HTMLField()),
            ],
        ),
        migrations.AlterField(
            model_name='img',
            name='pic',
            field=models.ImageField(upload_to=''),
        ),
    ]
