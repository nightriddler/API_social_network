# Generated by Django 3.2.2 on 2021-05-10 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20210510_1957'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='slug',
            field=models.SlugField(blank=True, null=True, verbose_name='Слаг'),
        ),
    ]
