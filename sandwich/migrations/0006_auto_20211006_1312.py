# Generated by Django 3.1.5 on 2021-10-06 04:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sandwich', '0005_auto_20211006_1235'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pay',
            name='card_payment',
            field=models.CharField(choices=[('선택안함', '선택안함'), ('FALSE', 'FALSE'), ('TRUE', 'TRUE')], default='N', max_length=10, verbose_name='카드결제여부'),
        ),
    ]
