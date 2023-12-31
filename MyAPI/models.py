from django.db import models


# Create your models here.
class Approvals(models.Model):
    GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female')
    )
    MARRIED_CHOICES = (
        ('Yes', 'Yes'),
        ('No', 'No')
    )
    GRADUATED_CHOICES = (
        ('Graduate', 'Graduate'),
        ('Not_Graduate', 'Not_Graduate')
    )
    SELFEMPLOYED_CHOICES = (
        ('Yes', 'Yes'),
        ('No', 'No')
    )
    CREDIT_CHOICES = (
        (0, '0'),
        (1, '1'),
        (2, '2'),
        (3, '3')
    )
    PROPERTY_CHOICES = (
        ('Rural', 'Rural'),
        ('Semiurban', 'Semiurban'),
        ('Urban', 'Urban')
    )

    Firstname = models.CharField(max_length=15)
    Lastname = models.CharField(max_length=15)
    Dependents = models.IntegerField(default=0)
    ApplicantIncome = models.IntegerField(default=0)
    CoapplicantIncome = models.IntegerField(default=0)
    LoanAmount = models.IntegerField(default=0)
    Loan_Amount_Term = models.IntegerField(default=0)
    Credit_History = models.IntegerField(choices=CREDIT_CHOICES)
    Gender = models.CharField(max_length=15, choices=GENDER_CHOICES)
    Married = models.CharField(max_length=15, choices=MARRIED_CHOICES)
    Education = models.CharField(max_length=15, choices=GRADUATED_CHOICES)
    Self_Employed = models.CharField(max_length=15, choices=SELFEMPLOYED_CHOICES)
    Property_Area = models.CharField(max_length=15, choices=PROPERTY_CHOICES)

    def __str__(self):
        return self.Firstname
