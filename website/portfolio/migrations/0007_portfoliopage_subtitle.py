# Generated by Django 2.0.9 on 2018-10-06 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0006_portfoliopage_headline'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfoliopage',
            name='subtitle',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]