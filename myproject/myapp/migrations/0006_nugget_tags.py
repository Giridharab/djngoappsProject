# Generated by Django 4.2.1 on 2023-05-24 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_remove_nugget_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='nugget',
            name='tags',
            field=models.CharField(max_length=200, null=True),
        ),
    ]