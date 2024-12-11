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

class Districtaveragescores(models.Model):
    districtyearid = models.AutoField(db_column='DistrictYearID', primary_key=True)  # Field name made lowercase.
    districtid = models.IntegerField(db_column='DistrictID')  # Field name made lowercase.
    year = models.IntegerField(db_column='Year')  # Field name made lowercase.
    avgenglish = models.TextField(db_column='AvgEnglish', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    avgmath = models.TextField(db_column='AvgMath', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    avgscience = models.TextField(db_column='AvgScience', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'DistrictAverageScores'


class Districtdata(models.Model):
    district_id = models.AutoField(db_column='District_ID', primary_key=True)  # Field name made lowercase.
    size = models.CharField(db_column='Size', blank=True, null=True, max_length=255)  # 指定max_length=255，字段名转为小写
    name = models.CharField(db_column='Name', blank=True, null=True, max_length=255)  # 指定max_length=255，字段名转为 lowercase
    address = models.CharField(db_column='Address', blank=True, null=True, max_length=255)  # 指定max_length=255，字段名转为 lowercase
    phonenumber = models.CharField(db_column='PhoneNumber', blank=True, null=True, max_length=255)  # 指定max_length=255，字段名转为 lowercase
    numofstudents = models.IntegerField(db_column='NumOfStudents', blank=True, null=True)  # Field name made lowercase.
    gifted = models.DecimalField(db_column='Gifted', max_digits=10, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    americanindian = models.DecimalField(db_column='AmericanIndian', max_digits=10, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    alaskannative = models.DecimalField(db_column='AlaskanNative', max_digits=10, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    asian = models.DecimalField(db_column='Asian', max_digits=10, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    blackafricanamerican = models.DecimalField(db_column='BlackAfricanAmerican', max_digits=10, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    hispanic = models.DecimalField(db_column='Hispanic', max_digits=10, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    twoormoreraces = models.DecimalField(db_column='TwoOrMoreRaces', max_digits=10, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    white = models.DecimalField(db_column='White', max_digits=10, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    economicallydisadvantaged = models.DecimalField(db_column='EconomicallyDisadvantaged', max_digits=10, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    englishlearner = models.DecimalField(db_column='EnglishLearner', max_digits=10, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    specialed = models.DecimalField(db_column='SpecialEd', max_digits=10, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    homeless = models.DecimalField(db_column='Homeless', max_digits=10, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    fostercare = models.DecimalField(db_column='FosterCare', max_digits=10, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    military = models.DecimalField(db_column='Military', max_digits=10, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pctadvanced = models.DecimalField(db_column='PctAdvanced', max_digits=10, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pctproficient = models.DecimalField(db_column='PctProficient', max_digits=10, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pctbasic = models.DecimalField(db_column='PctBasic', max_digits=10, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pctbelowbasic = models.DecimalField(db_column='PctBelowBasic', max_digits=10, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float

    class Meta:
        managed = False
        db_table = 'DistrictData'


class Districtidtoyear(models.Model):
    district_id = models.AutoField(db_column='District_ID', primary_key=True)  # Field name made lowercase.
    yr_2024 = models.IntegerField(db_column='Yr_2024', blank=True, null=True)  # Field name made lowercase.
    yr_2023 = models.IntegerField(db_column='Yr_2023', blank=True, null=True)  # Field name made lowercase.
    yr_2022 = models.IntegerField(db_column='Yr_2022', blank=True, null=True)  # Field name made lowercase.
    yr_2021 = models.IntegerField(db_column='Yr_2021', blank=True, null=True)  # Field name made lowercase.
    yr_2020 = models.IntegerField(db_column='Yr_2020', blank=True, null=True)  # Field name made lowercase.
    yr_2019 = models.IntegerField(db_column='Yr_2019', blank=True, null=True)  # Field name made lowercase.
    yr_2018 = models.IntegerField(db_column='Yr_2018', blank=True, null=True)  # Field name made lowercase.
    yr_2017 = models.IntegerField(db_column='Yr_2017', blank=True, null=True)  # Field name made lowercase.
    yr_2016 = models.IntegerField(db_column='Yr_2016', blank=True, null=True)  # Field name made lowercase.
    yr_2015 = models.IntegerField(db_column='Yr_2015', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DistrictIDToYear'


class Districtperformance(models.Model):
    performanceid = models.AutoField(db_column='PerformanceID', primary_key=True)  # Field name made lowercase.
    districtid = models.ForeignKey(Districtdata, models.DO_NOTHING, db_column='DistrictID', blank=True, null=True)  # Field name made lowercase.
    yr = models.IntegerField(db_column='Yr', blank=True, null=True)  # Field name made lowercase.
    studentgroupname = models.TextField(db_column='StudentGroupName', blank=True, null=True)  # Field name made lowercase.
    nscored = models.IntegerField(db_column='NScored', blank=True, null=True)  # Field name made lowercase.
    pctadvanced = models.FloatField(db_column='PctAdvanced', blank=True, null=True)  # Field name made lowercase.
    pctproficient = models.FloatField(db_column='PctProficient', blank=True, null=True)  # Field name made lowercase.
    pctbasic = models.FloatField(db_column='PctBasic', blank=True, null=True)  # Field name made lowercase.
    pctbelowbasic = models.FloatField(db_column='PctBelowBasic', blank=True, null=True)  # Field name made lowercase.
    growth = models.FloatField(db_column='Growth', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DistrictPerformance'


class Districttoschool(models.Model):
    districtid = models.OneToOneField(Districtdata, models.DO_NOTHING, db_column='DistrictID', primary_key=True)  # Field name made lowercase. The composite primary key (DistrictID, SchoolID) found, that is not supported. The first column is selected.
    schoolid = models.IntegerField(db_column='SchoolID', blank=True, null=True)  # Field name made lowercase.
    private = models.BooleanField(db_column='Private', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DistrictToSchool'


class Dropoutrates(models.Model):
    aunyear = models.OneToOneField(Districtidtoyear, models.DO_NOTHING, db_column='AUNyear', primary_key=True)  # Field name made lowercase.
    dropoutpercent = models.TextField(db_column='DropoutPercent', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    maledropouts = models.IntegerField(db_column='MaleDropouts', blank=True, null=True)  # Field name made lowercase.
    femaledropouts = models.IntegerField(db_column='FemaleDropouts', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DropOutRates'


class Lowincomeschoolsdesignatedforteacherloan(models.Model):
    schoolnumber = models.AutoField(db_column='SchoolNumber', primary_key=True)  # Field name made lowercase.
    percent = models.DecimalField(db_column='Percent', max_digits=10, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float

    class Meta:
        managed = False
        db_table = 'LowIncomeSchoolsDesignatedforTeacherLoan'


class Percentlowincomebyschool(models.Model):
    schoolnumber = models.OneToOneField('Schooldata', models.DO_NOTHING, db_column='SchoolNumber', primary_key=True)  # Field name made lowercase.
    percent = models.TextField(db_column='Percent', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'PercentLowIncomeBySchool'


class Publicdropoutrates(models.Model):
    schl = models.AutoField(db_column='Schl', primary_key=True)  # Field name made lowercase.
    maledropouts = models.IntegerField(db_column='MaleDropouts', blank=True, null=True)  # Field name made lowercase.
    femaledropouts = models.IntegerField(db_column='FemaleDropouts', blank=True, null=True)  # Field name made lowercase.
    totaldropouts = models.IntegerField(db_column='TotalDropouts', blank=True, null=True)  # Field name made lowercase.
    dropoutrate = models.DecimalField(db_column='DropOutRate', max_digits=10, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float

    class Meta:
        managed = False
        db_table = 'PublicDropOutRates'

class Schooldatas(models.Model):
    districtname = models.CharField(db_column='DistrictName', blank=True, null=True, max_length=255)  # 指定max_length=255，字段名转为小写
    aun = models.IntegerField(db_column='AUN', blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', blank=True, null=True, max_length=255)  # 指定max_length=255，字段名转为小写
    schl = models.IntegerField(db_column='Schl')  # Field name made lowercase.
    schoolname = models.CharField(db_column='SchoolName', blank=True, null=True, max_length=255)  # 指定max_length=255，字段名转为 lowercase
    schooladdressstreet = models.CharField(db_column='SchoolAddressStreet', blank=True, null=True, max_length=255)  # 指定max_length=255，字段名转为 lowercase
    schooladdresscity = models.CharField(db_column='SchoolAddressCity', blank=True, null=True, max_length=255)  # 指定max_length=255，字段名转为 lowercase
    schooladdressstate = models.CharField(db_column='SchoolAddressState', blank=True, null=True, max_length=255)  # 指定max_length=255，字段名转为 lowercase
    schoolzipcode = models.CharField(db_column='SchoolZipCode', blank=True, null=True, max_length=255)  # 指定max_length=255，字段名转为 lowercase
    website = models.CharField(db_column='Website', blank=True, null=True, max_length=255)  # 指定max_length=255，字段名转为 lowercase
    telephonenumber = models.CharField(db_column='TelephoneNumber', blank=True, null=True, max_length=255)  # 指定max_length=255，字段名转为 lowercase
    gradesoffered = models.CharField(db_column='GradesOffered', blank=True, null=True, max_length=255)  # 指定max_length=255，字段名转为 lowercase
    titleschool = models.BooleanField(db_column='TitleSchool', blank=True, null=True)  # Field name made lowercase.
    schoolenrollment = models.IntegerField(db_column='SchoolEnrollment', blank=True, null=True)  # Field name made lowercase.
    percentgifted = models.DecimalField(db_column='PercentGifted', max_digits=10, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    studentsintermediate = models.CharField(db_column='StudentsIntermediate', blank=True, null=True, max_length=255)  # 指定max_length=255，字段名转为 lowercase
    nativeamericanalaskan = models.DecimalField(db_column='NativeAmericanAlaskan', max_digits=10, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    asian = models.DecimalField(db_column='Asian', max_digits=10, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    blackafricanamerican = models.DecimalField(db_column='BlackAfricanAmerican', max_digits=10, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    hispanic = models.DecimalField(db_column='Hispanic', max_digits=10, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    twoormoreraces = models.DecimalField(db_column='TwoOrMoreRaces', max_digits=10, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    white = models.DecimalField(db_column='White', max_digits=10, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pacificislander = models.DecimalField(db_column='PacificIslander', max_digits=10, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    economicallydisadvantaged = models.DecimalField(db_column='EconomicallyDisadvantaged', max_digits=10, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal.fields as float
    englishlearner = models.DecimalField(db_column='EnglishLearner', max_digits=10, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal.fields as float
    specialeducation = models.DecimalField(db_column='SpecialEducation', max_digits=10, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal.fields as float
    femaleschool = models.BooleanField(db_column='FemaleSchool', blank=True, null=True)  # Field name made lowercase.
    maleschool = models.BooleanField(db_column='MaleSchool', blank=True, null=True)  # Field name made lowercase.
    fostercare = models.DecimalField(db_column='FosterCare', max_digits=10, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal.fields as float
    homeless = models.DecimalField(db_column='Homeless', max_digits=10, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal.fields as float
    militaryconnected = models.DecimalField(db_column='MilitaryConnected', max_digits=10, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal.fields as float

    class Meta:
        managed = False
        db_table = 'SchoolData'


class Schoolperformancee(models.Model):
    performance_id = models.AutoField(db_column='Performance_id', primary_key=True)  # 移除null=True，符合主键规范，字段名转为小写
    yr = models.IntegerField(db_column='Yr', blank=True, null=True)  # Field name made lowercase.
    studentgroupname = models.TextField(db_column='StudentGroupName', blank=True, null=True)  # Field name made lowercase.
    nscored = models.IntegerField(db_column='NScored', blank=True, null=True)  # Field name made lowercase.
    pctadvanced = models.FloatField(db_column='PctAdvanced', blank=True, null=True)  # Field name made lowercase.
    pctproficient = models.FloatField(db_column='PctProficient', blank=True, null=True)  # Field name made lowercase.
    pctbasic = models.FloatField(db_column='PctBasic', blank=True, null=True)  # Field name made lowercase.
    pctbelowbasic = models.FloatField(db_column='PctBelowBasic', blank=True, null=True)  # Field name made lowercase.
    growth = models.FloatField(db_column='Growth', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SchoolPerformanceE'


class Schoolperformanceehup(models.Model):
    schl = models.AutoField(db_column='Schl', primary_key=True)  # 移除null=True，符合主键规范，字段名转为小写
    grade = models.CharField(db_column='Grade', blank=True, null=True, max_length=255)  # 指定max_length=255，字段名转为小写
    studentgroupname = models.CharField(db_column='StudentGroupName', blank=True, null=True, max_length=255)  # 指定max_length=255，字段名转为小写
    nscored = models.IntegerField(db_column='NScored', blank=True, null=True)  # Field name made lowercase.
    pctadvanced = models.DecimalField(db_column='PctAdvanced', max_digits=10, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pctproficient = models.DecimalField(db_column='PctProficient', max_digits=10, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pctbasic = models.DecimalField(db_column='PctBasic', max_digits=10, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pctbelowbasic = models.DecimalField(db_column='PctBelowBasic', max_digits=10, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    growth = models.DecimalField(db_column='Growth', max_digits=10, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float

    class Meta:
        managed = False
        db_table = 'SchoolPerformanceEHUP'


class Schoolperformanceeupf(models.Model):
    performance_id = models.AutoField(db_column='Performance_id', primary_key=True)  # 移除null=True，符合主键规范，字段名转为小写
    yr = models.IntegerField(db_column='Yr', blank=True, null=True)  # Field name made lowercase.
    studentgroupname = models.TextField(db_column='StudentGroupName', blank=True, null=True)  # Field name made lowercase.
    nscored = models.IntegerField(db_column='NScored', blank=True, null=True)  # Field name made lowercase.
    pctadvanced = models.DecimalField(db_column='PctAdvanced', max_digits=10, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pctproficient = models.DecimalField(db_column='PctProficient', max_digits=10, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pctbasic = models.DecimalField(db_column='PctBasic', max_digits=10, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pctbelowbasic = models.DecimalField(db_column='PctBelowBasic', max_digits=10, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    growth = models.TextField(db_column='Growth', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'SchoolPerformanceEUPF'


class Schoolperformancem(models.Model):
    performance_id = models.AutoField(db_column='Performance_id', primary_key=True)  # 移除null=True，符合主键规范，字段名转为小写
    yr = models.IntegerField(db_column='Yr', blank=True, null=True)  # Field name made lowercase.
    studentgroupname = models.TextField(db_column='StudentGroupName', blank=True, null=True)  # Field name made lowercase.
    nscored = models.IntegerField(db_column='NScored', blank=True, null=True)  # Field name made lowercase.
    pctadvanced = models.DecimalField(db_column='PctAdvanced', max_digits=10, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pctproficient = models.DecimalField(db_column='PctProficient', max_digits=10, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pctbasic = models.DecimalField(db_column='PctBasic', max_digits=10, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pctbelowbasic = models.DecimalField(db_column='PctBelowBasic', max_digits=10, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    growth = models.TextField(db_column='Growth', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'SchoolPerformanceM'


class Schoolperformancemhup(models.Model):
    schl = models.AutoField(db_column='Schl', primary_key=True)  # 移除null=True，符合主键规范，字段名转为 lowercase
    grade = models.CharField(db_column='Grade', blank=True, null=True, max_length=255)  # 指定max_length=255，字段名转为 lowercase
    studentgroupname = models.CharField(db_column='StudentGroupName', blank=True, null=True, max_length=255)  # 指定max_length=255，字段名转为 lowercase
    nscored = models.IntegerField(db_column='NScored', blank=True, null=True)  # Field name made lowercase.
    pctadvanced = models.DecimalField(db_column='PctAdvanced', max_digits=10, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pctproficient = models.DecimalField(db_column='PctProficient', max_digits=10, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pctbasic = models.DecimalField(db_column='PctBasic', max_digits=10, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pctbelowbasic = models.DecimalField(db_column='PctBelowBasic', max_digits=10, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    growth = models.DecimalField(db_column='Growth', max_digits=10, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float

    class Meta:
        managed = False
        db_table = 'SchoolPerformanceMHUP'


class Schoolperformancemupf(models.Model):
    performance_id = models.AutoField(db_column='Performance_id', primary_key=True)  # 移除null=True，符合主键规范，字段名转为小写
    yr = models.IntegerField(db_column='Yr', blank=True, null=True)  # Field name made lowercase.
    studentgroupname = models.TextField(db_column='StudentGroupName', blank=True, null=True)  # Field name made lowercase.
    nscored = models.IntegerField(db_column='NScored', blank=True, null=True)  # Field name made lowercase.
    pctadvanced = models.DecimalField(db_column='PctAdvanced', max_digits=10, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits和decimal_places为猜测值，因数据库将小数字段当作float处理
    pctproficient = models.DecimalField(db_column='PctProficient', max_digits=10, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits和decimal_places为猜测值，因数据库将小数字段当作float处理
    pctbasic = models.DecimalField(db_column='PctBasic', max_digits=10, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits和decimal_places为猜测值，因数据库将小数字段当作float处理
    pctbelowbasic = models.DecimalField(db_column='PctBelowBasic', max_digits=10, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits和decimal_places为猜测值，因数据库将小数字段当作float处理
    growth = models.TextField(db_column='Growth', blank=True, null=True)  # Field name made lowercase. 此字段类型为猜测

    class Meta:
        managed = False
        db_table = 'SchoolPerformanceMUPF'


class Schoolperformances(models.Model):
    performance_id = models.AutoField(db_column='Performance_id', primary_key=True)  # 移除null=True，符合主键规范，字段名转为小写
    yr = models.IntegerField(db_column='Yr', blank=True, null=True)  # Field name made lowercase.
    studentgroupname = models.TextField(db_column='StudentGroupName', blank=True, null=True)  # Field name made lowercase.
    nscored = models.IntegerField(db_column='NScored', blank=True, null=True)  # Field name made lowercase.
    pctadvanced = models.DecimalField(db_column='PctAdvanced', max_digits=10, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits和decimal_places为猜测值，因数据库将小数字段当作float处理
    pctproficient = models.DecimalField(db_column='PctProficient', max_digits=10, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits和decimal_places为猜测值，因数据库将小数字段当作float处理
    pctbasic = models.DecimalField(db_column='PctBasic', max_digits=10, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits和decimal_places为猜测值，因数据库将小数字段当作float处理
    pctbelowbasic = models.DecimalField(db_column='PctBelowBasic', max_digits=10, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits和decimal_places为猜测值，因数据库将小数字段当作float处理
    growth = models.TextField(db_column='Growth', blank=True, null=True)  # Field name made lowercase. 此字段类型为猜测

    class Meta:
        managed = False
        db_table = 'SchoolPerformanceS'


class Schoolperformanceshup(models.Model):
    schl = models.AutoField(db_column='Schl', primary_key=True)  # 移除null=True，符合主键规范，字段名转为 lowercase
    grade = models.CharField(db_column='Grade', blank=True, null=True, max_length=255)  # 指定max_length=255，字段名转为 lowercase
    studentgroupname = models.CharField(db_column='StudentGroupName', blank=True, null=True, max_length=255)  # 指定max_length=255，字段名转为 lowercase
    nscored = models.IntegerField(db_column='NScored', blank=True, null=True)  # Field name made lowercase.
    pctadvanced = models.DecimalField(db_column='PctAdvanced', max_digits=10, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits和decimal_places为猜测值，因数据库将小数字段当作float处理
    pctproficient = models.DecimalField(db_column='PctProficient', max_digits=10, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits和decimal_places为猜测值，因数据库将小数字段当作float处理
    pctbasic = models.DecimalField(db_column='PctBasic', max_digits=10, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits和decimal_places为猜测值，因数据库将小数字段当作float处理
    pctbelowbasic = models.DecimalField(db_column='PctBelowBasic', max_digits=10, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits和decimal_places为猜测值，因数据库将小数字段当作float处理
    growth = models.DecimalField(db_column='Growth', max_digits=10, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits和decimal_places为猜测值，因数据库将小数字段当作float处理

    class Meta:
        managed = False
        db_table = 'SchoolPerformanceSHUP'


class Schoolperformancesupf(models.Model):
    performance_id = models.AutoField(db_column='Performance_id', primary_key=True)  # 移除null=True，符合主键规范，字段名转为 lowercase
    yr = models.IntegerField(db_column='Yr', blank=True, null=True)  # Field name made lowercase.
    studentgroupname = models.TextField(db_column='StudentGroupName', blank=True, null=True)  # Field name made lowercase.
    nscored = models.IntegerField(db_column='NScored', blank=True, null=True)  # Field name made lowercase.
    pctadvanced = models.DecimalField(db_column='PctAdvanced', max_digits=10, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits和decimal_places为猜测值，因数据库将小数字段当作float处理
    pctproficient = models.DecimalField(db_column='PctProficient', max_digits=10, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits和decimal_places为猜测值，因数据库将小数字段当作float处理
    pctbasic = models.DecimalField(db_column='PctBasic', max_digits=10, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits和decimal_places为猜测值，因数据库将小数字段当作float处理
    pctbelowbasic = models.DecimalField(db_column='PctBelowBasic', max_digits=10, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits和decimal_places为猜测值，因数据库将小数字段当作float处理
    growth = models.TextField(db_column='Growth', blank=True, null=True)  # Field name made lowercase. 此字段类型为猜测

    class Meta:
        managed = False
        db_table = 'SchoolPerformanceSUPF'