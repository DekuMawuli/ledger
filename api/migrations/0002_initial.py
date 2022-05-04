# Generated by Django 4.0.4 on 2022-05-03 20:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('api', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='internaltransfer',
            name='customer',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='internaltransfer',
            name='receiving_account',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='receiving_account', to='api.account'),
        ),
        migrations.AddField(
            model_name='internaltransfer',
            name='sender_account',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='sender_account', to='api.account'),
        ),
        migrations.AddField(
            model_name='externaltransfer',
            name='receiver',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='receiver', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='externaltransfer',
            name='receiver_account',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='external_receiving_account', to='api.account'),
        ),
        migrations.AddField(
            model_name='externaltransfer',
            name='sender',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='sender', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='externaltransfer',
            name='sender_account',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='external_sender_account', to='api.account'),
        ),
        migrations.AddField(
            model_name='account',
            name='customer',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
