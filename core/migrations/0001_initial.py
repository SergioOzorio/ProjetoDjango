# Generated by Django 5.0.1 on 2024-02-01 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='nome')),
                ('price', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='preço')),
                ('stock', models.IntegerField(verbose_name='Quantidade em estoque')),
            ],
        ),
    ]
