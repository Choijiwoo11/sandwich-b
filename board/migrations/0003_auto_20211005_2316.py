# Generated by Django 3.1.5 on 2021-10-05 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0002_auto_20210816_1710'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False, verbose_name='파일번호'),
        ),
    ]
