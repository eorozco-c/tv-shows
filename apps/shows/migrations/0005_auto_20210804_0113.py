# Generated by Django 2.2.4 on 2021-08-04 05:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shows', '0004_auto_20210804_0106'),
    ]

    operations = [
        migrations.AlterField(
            model_name='show',
            name='title',
            field=models.CharField(max_length=50),
        ),
    ]