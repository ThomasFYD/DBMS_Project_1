from django.db import models

# Create your models here.
# school_data/models.py


class SchoolData(models.Model):
    district_name = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    aun = models.IntegerField()
    schl = models.IntegerField(primary_key=True)
    school_address_street = models.CharField(max_length=255)
    school_address_city = models.CharField(max_length=255)
    school_zip_code = models.CharField(max_length=10)
    school_enrollment = models.DecimalField(max_digits=10, decimal_places=2)
    percent_gifted_student = models.DecimalField(max_digits=5, decimal_places=2)

    # New fields allowing null values
    low_income_percentage = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    teacher_loan_cancellations = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    percent_students_low_income = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    test_scores = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    dropout_rate = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return self.name
