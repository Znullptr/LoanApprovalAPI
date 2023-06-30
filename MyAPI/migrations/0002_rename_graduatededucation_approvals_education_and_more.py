# Generated by Django 4.2.2 on 2023-06-13 02:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyAPI', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='approvals',
            old_name='graduatededucation',
            new_name='Education',
        ),
        migrations.RenameField(
            model_name='approvals',
            old_name='firstname',
            new_name='Firstname',
        ),
        migrations.RenameField(
            model_name='approvals',
            old_name='gender',
            new_name='Gender',
        ),
        migrations.RenameField(
            model_name='approvals',
            old_name='lastname',
            new_name='Lastname',
        ),
        migrations.RenameField(
            model_name='approvals',
            old_name='married',
            new_name='Married',
        ),
        migrations.RenameField(
            model_name='approvals',
            old_name='area',
            new_name='Property_Area',
        ),
        migrations.RenameField(
            model_name='approvals',
            old_name='selfemployed',
            new_name='Self_Employed',
        ),
        migrations.RemoveField(
            model_name='approvals',
            name='applicantincome',
        ),
        migrations.RemoveField(
            model_name='approvals',
            name='coapplicantincome',
        ),
        migrations.RemoveField(
            model_name='approvals',
            name='credithistory',
        ),
        migrations.RemoveField(
            model_name='approvals',
            name='dependants',
        ),
        migrations.RemoveField(
            model_name='approvals',
            name='loanamt',
        ),
        migrations.RemoveField(
            model_name='approvals',
            name='loanterm',
        ),
        migrations.AddField(
            model_name='approvals',
            name='Credit_History',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='approvals',
            name='Dependents',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='approvals',
            name='LoanAmount',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='approvals',
            name='Loan_Amount_Term',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='approvals',
            name='ApplicantIncome',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='approvals',
            name='CoapplicantIncome',
            field=models.IntegerField(default=0),
        ),
    ]