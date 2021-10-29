# Generated by Django 3.1.5 on 2021-10-05 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sandwich', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False, verbose_name='카테고리번호'),
        ),
        migrations.AlterField(
            model_name='editor',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False, verbose_name='번호'),
        ),
        migrations.AlterField(
            model_name='pay',
            name='card_payment',
            field=models.CharField(choices=[('TRUE', 'TRUE'), ('FALSE', 'FALSE'), ('선택안함', '선택안함')], default='N', max_length=10, verbose_name='카드결제여부'),
        ),
    ]