# Generated by Django 3.2.5 on 2021-08-21 01:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_auto_20210821_1139'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsstory',
            name='image_url',
            field=models.CharField(default='https://picsum.photos/600', max_length=140),
        ),
        migrations.AlterField(
            model_name='recentupdate',
            name='image_url',
            field=models.CharField(default='https://picsum.photos/600', max_length=140),
        ),
    ]
