# Generated by Django 4.1.5 on 2023-01-25 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.CharField(max_length=100, unique=True)),
                ('order_amount', models.PositiveBigIntegerField()),
                ('status', models.CharField(choices=[('FAILED', 'failed'), ('SUCESS', 'SUCESS'), ('pending', 'pending')], default='pending', max_length=30)),
            ],
        ),
    ]
