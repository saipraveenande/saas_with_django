# Generated by Django 4.2.2 on 2023-07-30 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_remove_donate_email_donate_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='donate',
            name='order_id',
            field=models.CharField(default=0, max_length=70),
            preserve_default=False,
        ),
    ]
