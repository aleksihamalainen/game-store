# Generated by Django 3.0.2 on 2020-02-20 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0007_transaction_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='state',
            field=models.TextField(default=''),
        ),
    ]
