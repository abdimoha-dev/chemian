# Generated by Django 3.1.1 on 2020-10-29 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dash', '0007_auto_20201029_0800'),
    ]

    operations = [
        migrations.AlterField(
            model_name='title',
            name='main_image',
            field=models.ImageField(null=True, upload_to='dash/images'),
        ),
    ]
