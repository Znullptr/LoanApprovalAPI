# Generated by Django 4.2.2 on 2023-06-22 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyAPI', '0002_rename_graduatededucation_approvals_education_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='approvals',
            name='Credit_History',
            field=models.IntegerField(choices=[('0', 0), ('1', 1), ('2', 2), ('3', 3)], default=0),
        ),
    ]
