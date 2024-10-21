# Generated by Django 5.0.6 on 2024-05-15 23:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0002_rename_picture_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='name',
            field=models.CharField(max_length=200, unique=True),
        ),
        migrations.CreateModel(
            name='Rectangle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('height', models.IntegerField(default=0)),
                ('width', models.IntegerField(default=0)),
                ('color', models.CharField(max_length=100)),
                ('x', models.IntegerField(default=0)),
                ('y', models.IntegerField(default=0)),
                ('picture', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rectangles', to='images.image')),
            ],
        ),
        migrations.DeleteModel(
            name='Square',
        ),
    ]