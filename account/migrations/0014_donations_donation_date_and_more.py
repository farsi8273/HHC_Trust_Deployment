# Generated by Django 4.1.7 on 2023-05-26 04:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0013_alter_certificate_80g_created_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='donations',
            name='donation_date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='certificate_80g',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]