# Generated by Django 5.0.6 on 2024-05-24 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Company_Staff', '0005_remove_retainerinvoice_customer_name1'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment_made_bills',
            name='date',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]
