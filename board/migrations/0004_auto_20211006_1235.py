# Generated by Django 3.1.5 on 2021-10-06 03:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0003_auto_20211005_2316'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='post_no',
            new_name='post',
        ),
    ]
