# Generated by Django 3.0.2 on 2020-02-07 14:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
        ('games', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='developer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='games', to='users.Developer'),
        ),
    ]
