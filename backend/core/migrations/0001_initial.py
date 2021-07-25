# Generated by Django 3.2.5 on 2021-07-16 18:05

import datetime
import django.contrib.auth.models
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Seller',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('description', models.TextField(max_length=100)),
                ('type', models.CharField(choices=[('AUTO', 'Auto insurance'), ('HOME', 'Home insurance'), ('LIFE', 'Life insurance')], max_length=4)),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('percentage_rate', models.PositiveSmallIntegerField(validators=[django.core.validators.MaxValueValidator(100)])),
                ('insurance_period', models.DurationField(choices=[(datetime.timedelta(days=90), 'Три месяца'), (datetime.timedelta(days=365), 'Шесть месяцев'), (datetime.timedelta(days=365), 'Двенадцать месяцев')])),
                ('published', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
                ('slug', models.SlugField(unique=True)),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='core.seller')),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('telephone', models.CharField(blank=True, max_length=17)),
                ('email', models.EmailField(max_length=254)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='customers', to='core.product')),
            ],
        ),
    ]