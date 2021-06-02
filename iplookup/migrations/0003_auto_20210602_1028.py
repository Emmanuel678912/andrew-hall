# Generated by Django 3.2.3 on 2021-06-02 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iplookup', '0002_auto_20210602_1025'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tablea',
            name='column2',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='tablea',
            name='column3',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='tableb',
            name='column2',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='tableb',
            name='column3',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='tablec',
            name='column2',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='tablec',
            name='column3',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='tabled',
            name='first_octet',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='tabled',
            name='fourth_octet',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='tabled',
            name='second_octet',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='tabled',
            name='subnet_mask',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='tabled',
            name='third_octet',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='tablee',
            name='first_octet',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='tablee',
            name='fourth_octet',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='tablee',
            name='second_octet',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='tablee',
            name='subnet_mask',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='tablee',
            name='third_octet',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='tablef',
            name='first_octet',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='tablef',
            name='fourth_octet',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='tablef',
            name='second_octet',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='tablef',
            name='subnet_mask',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='tablef',
            name='third_octet',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='tablef',
            name='variable',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='tableg',
            name='column2',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='tableg',
            name='column3',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
