# Generated by Django 3.2.12 on 2023-03-31 09:56

from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contacts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('subject', models.CharField(max_length=300)),
                ('massage', models.TextField(max_length=300)),
                ('created_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('Created_by', models.CharField(blank=True, max_length=200)),
                ('updated_by', models.CharField(blank=True, max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Feature_Campaigns',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=300)),
                ('description', models.TextField(max_length=300)),
                ('image', models.ImageField(upload_to='static/account/image/featured/')),
                ('created_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('Created_by', models.CharField(blank=True, max_length=200)),
                ('updated_by', models.CharField(blank=True, max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='static/account/image/gallery/')),
                ('created_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('Created_by', models.CharField(blank=True, max_length=200)),
                ('updated_by', models.CharField(blank=True, max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Volunteers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('father_name', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
                ('region', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('pincode', models.IntegerField()),
                ('education', models.CharField(choices=[('undergraduate ', 'Undergraduate '), ('postgraduate', 'Postgraduate'), ('other', 'Other')], default='Undergraduate', max_length=32, verbose_name='Choose your Education')),
                ('image', models.ImageField(upload_to='static/account/image/volunteers/')),
                ('email', models.EmailField(max_length=254)),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, unique=True)),
                ('visible_flag', models.BooleanField(default=False)),
                ('created_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('Created_by', models.CharField(blank=True, max_length=200)),
                ('updated_by', models.CharField(blank=True, max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Social_Voluteers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account', models.CharField(choices=[('fa-facebook-f ', 'Facebook '), ('fa-instagram', 'Instagram'), ('fa-linkedin-in', 'LinkedIn'), ('fa-twitter', 'Twitter')], default='Facebook', max_length=32, verbose_name='Choose your social media account')),
                ('url', models.URLField(max_length=300)),
                ('created_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('Created_by', models.CharField(blank=True, max_length=200)),
                ('updated_by', models.CharField(blank=True, max_length=200)),
                ('volunteers', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.volunteers')),
            ],
        ),
        migrations.CreateModel(
            name='Donation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('country', models.CharField(max_length=100)),
                ('region', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('pincode', models.IntegerField()),
                ('amount', models.IntegerField()),
                ('reference', models.IntegerField(default=0, null=True)),
                ('Certificate_80G', models.BooleanField(default=False)),
                ('created_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('Created_by', models.CharField(blank=True, max_length=200)),
                ('updated_by', models.CharField(blank=True, max_length=200)),
                ('campaigns', models.ForeignKey(default='Education', on_delete=django.db.models.deletion.CASCADE, to='account.feature_campaigns')),
            ],
        ),
    ]
