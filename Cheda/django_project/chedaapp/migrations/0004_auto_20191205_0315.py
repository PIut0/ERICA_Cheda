# Generated by Django 2.2.7 on 2019-12-04 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chedaapp', '0003_nak'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nak',
            name='etc',
            field=models.TextField(blank=True, null=True),
        ),
    ]