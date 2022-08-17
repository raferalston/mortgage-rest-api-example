# Generated by Django 3.1.6 on 2022-08-17 09:20

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mortgage', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BankModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bank_name', models.CharField(max_length=50)),
                ('term_min', models.PositiveSmallIntegerField(default=10, validators=[django.core.validators.MinValueValidator(10), django.core.validators.MaxValueValidator(30)])),
                ('term_max', models.PositiveSmallIntegerField(default=30, validators=[django.core.validators.MinValueValidator(10), django.core.validators.MaxValueValidator(30)])),
                ('rate_min', models.DecimalField(decimal_places=1, default=1.8, max_digits=2)),
                ('rate_max', models.DecimalField(decimal_places=1, default=9.8, max_digits=2)),
                ('payment_min', models.PositiveIntegerField(default=1000000, validators=[django.core.validators.MinValueValidator(1000000), django.core.validators.MaxValueValidator(10000000)])),
                ('payment_max', models.PositiveIntegerField(default=10000000, validators=[django.core.validators.MinValueValidator(1000000), django.core.validators.MaxValueValidator(10000000)])),
            ],
            options={
                'verbose_name': 'Bank',
                'verbose_name_plural': 'Banks',
            },
        ),
        migrations.DeleteModel(
            name='Bank',
        ),
    ]
