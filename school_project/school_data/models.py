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
    # Add other fields as per your schema
    school_enrollment = models.DecimalField(max_digits=10, decimal_places=2)
    percent_gifted_student = models.DecimalField(max_digits=5, decimal_places=2)
    # Include other fields as required

    def __str__(self):
        return self.name
