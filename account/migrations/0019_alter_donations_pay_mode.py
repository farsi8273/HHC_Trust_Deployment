# Generated by Django 4.1.7 on 2023-09-11 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0018_alter_feature_campaigns_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donations',
            name='pay_mode',
            field=models.CharField(choices=[('Cash', 'Cash'), ('UPI', 'UPI'), ('Cheque', 'Cheque'), ('Net Banking', 'Net Banking'), ('Credit Card', 'CC'), ('Debit Card', 'ATM')], default='UPI', max_length=11),
        ),
    ]