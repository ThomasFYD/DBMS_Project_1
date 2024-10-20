# Generated by Django 5.2.dev20240911160443 on 2024-10-20 23:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school_data', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='schooldata',
            name='dropout_rate',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AddField(
            model_name='schooldata',
            name='low_income_percentage',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AddField(
            model_name='schooldata',
            name='percent_students_low_income',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AddField(
            model_name='schooldata',
            name='teacher_loan_cancellations',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AddField(
            model_name='schooldata',
            name='test_scores',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
    ]
