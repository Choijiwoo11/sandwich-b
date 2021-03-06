# Generated by Django 3.1.5 on 2021-10-06 03:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sandwich', '0003_auto_20211006_0325'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'ordering': ['date_joined'], 'verbose_name': 'User', 'verbose_name_plural': 'Users'},
        ),
        migrations.RenameField(
            model_name='inquiry',
            old_name='author_no',
            new_name='author',
        ),
        migrations.RenameField(
            model_name='inquiry',
            old_name='magazine_no',
            new_name='magazine',
        ),
        migrations.AlterField(
            model_name='pay',
            name='card_payment',
            field=models.CharField(choices=[('FALSE', 'FALSE'), ('선택안함', '선택안함'), ('TRUE', 'TRUE')], default='N', max_length=10, verbose_name='카드결제여부'),
        ),
    ]
