# Generated by Django 4.0.4 on 2022-05-03 22:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_alter_account_customer_acctransaction'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='acctransaction',
            name='account',
        ),
        migrations.AddField(
            model_name='acctransaction',
            name='account_num',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
