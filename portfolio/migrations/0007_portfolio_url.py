# Generated by Django 5.0.6 on 2024-07-09 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0006_portfolio'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfolio',
            name='url',
            field=models.URLField(default=2, verbose_name=''),
            preserve_default=False,
        ),
    ]
