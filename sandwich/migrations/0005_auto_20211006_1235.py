# Generated by Django 3.1.5 on 2021-10-06 03:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sandwich', '0004_auto_20211006_1216'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pay',
            name='card_payment',
            field=models.CharField(choices=[('TRUE', 'TRUE'), ('FALSE', 'FALSE'), ('선택안함', '선택안함')], default='N', max_length=10, verbose_name='카드결제여부'),
        ),
    ]