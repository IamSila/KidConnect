# Generated by Django 5.1.4 on 2024-12-09 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0009_alter_report_profilephoto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='profilePhoto',
            field=models.ImageField(default='media/media/parent-wife-child.png', upload_to='media'),
        ),
    ]
