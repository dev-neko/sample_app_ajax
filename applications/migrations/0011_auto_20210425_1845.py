# Generated by Django 3.1.7 on 2021-04-25 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applications', '0010_userdatamodel_md_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdatamodel',
            name='md_line_token',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
