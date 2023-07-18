# Generated by Django 4.2.3 on 2023-07-18 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0005_goodscategorybrand_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='goodscategorybrand',
            name='img',
        ),
        migrations.AddField(
            model_name='goodscategorybrand',
            name='image',
            field=models.ImageField(default='', max_length=200, upload_to='brands/'),
            preserve_default=False,
        ),
    ]
