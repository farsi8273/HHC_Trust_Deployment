# Generated by Django 3.2.12 on 2023-04-01 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_alter_donation_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donation',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
