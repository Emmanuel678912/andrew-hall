# Generated by Django 3.2.3 on 2021-06-12 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iplookup', '0013_alter_tablec_column4'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tablec',
            name='column4',
            field=models.CharField(blank=True, choices=[('Value 1', '1'), ('Value 2', '2')], max_length=255, null=True),
        ),
    ]
