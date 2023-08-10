# Generated by Django 4.2.2 on 2023-06-29 01:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alumni', '0002_dzolali'),
    ]

    operations = [
        migrations.CreateModel(
            name='leased',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Item_Name', models.CharField(max_length=255)),
                ('Brand_Name', models.CharField(max_length=255)),
                ('Recipient', models.CharField(max_length=255)),
                ('Department', models.CharField(max_length=255)),
                ('Quantity', models.IntegerField()),
                ('Receive_Date', models.DateField()),
                ('Return_Date', models.DateField()),
                ('Remark', models.TextField()),
            ],
        ),
    ]