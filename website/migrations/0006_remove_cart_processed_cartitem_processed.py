# Generated by Django 5.1.3 on 2024-12-02 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0005_remove_cartitem_processed'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='processed',
        ),
        migrations.AddField(
            model_name='cartitem',
            name='processed',
            field=models.BooleanField(default=False),
        ),
    ]
