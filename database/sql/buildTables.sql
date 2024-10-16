CREATE TABLE SchoolData (
    DistrictName VARCHAR,
    Name VARCHAR,
    AUN INT,
    Schl INT,
    SchoolName VARCHAR,
    SchoolAddressStreet VARCHAR,
    SchoolAddressCity VARCHAR,
    SchoolAddressState VARCHAR,
    SchoolZipCode VARCHAR,
    Website VARCHAR,
    TelephoneNumber VARCHAR,
    GradesOffered VARCHAR,
    TitleISchool VARCHAR,
    SchoolEnrollment INT,
    PercentGiftedStudents DECIMAL,
    IntermediateUnitName VARCHAR,
    IntermediateUnitWebsite VARCHAR,
    AmericanIndianAlaskanNative DECIMAL,
    Asian DECIMAL,
    BlackAfricanAmerican DECIMAL,
    Hispanic DECIMAL,
    TwoOrMoreRaces DECIMAL,
    White DECIMAL,
    NativeHawaiianPacificIslander DECIMAL,
    EconomicallyDisadvantaged DECIMAL,
    EnglishLearner DECIMAL,
    SpecialEducation DECIMAL,
    FemaleSchool DECIMAL,
    MaleSchool DECIMAL,
    FosterCare DECIMAL,
    Homeless DECIMAL,
    MilitaryConnected DECIMAL,
    PRIMARY KEY (AUN)
);

CREATE TABLE SchoolPerformanceE(
    Schl INT,
    Grade INT,
    StudentGroupName VARCHAR,
    NScored INT,
    PctAdvanced DECIMAL,
    PctProficient DECIMAL,
    PctBasic DECIMAL,
    PctBelowBasic DECIMAL,
    Growth DECIMAL,
    PRIMARY KEY (Schl )
);
CREATE TABLE SchoolPerformanceEHUP(
    Schl INT,
    Grade VARCHAR,
    StudentGroupName VARCHAR,
    NScored INT,
    PctAdvanced DECIMAL,
    PctProficient DECIMAL,
    PctBasic DECIMAL,
    PctBelowBasic DECIMAL,
    Growth DECIMAL,
    PRIMARY KEY (Schl )
);
CREATE TABLE SchoolPerformanceM(
    Schl INT,
    Grade VARCHAR,
    StudentGroupName VARCHAR,
    NScored INT,
    PctAdvanced DECIMAL,
    PctProficient DECIMAL,
    PctBasic DECIMAL,
    PctBelowBasic DECIMAL,
    Growth DECIMAL,
    PRIMARY KEY (Schl )
);
CREATE TABLE SchoolPerformanceMHUP(
    Schl INT,
    Grade VARCHAR,
    StudentGroupName VARCHAR,
    NScored INT,
    PctAdvanced DECIMAL,
    PctProficient DECIMAL,
    PctBasic DECIMAL,
    PctBelowBasic DECIMAL,
    Growth DECIMAL,
    PRIMARY KEY (Schl )
);
CREATE TABLE SchoolPerformanceS(
    Schl INT,
    Grade VARCHAR,
    StudentGroupName VARCHAR,
    NScored INT,
    PctAdvanced DECIMAL,
    PctProficient DECIMAL,
    PctBasic DECIMAL,
    PctBelowBasic DECIMAL,
    Growth DECIMAL,
    PRIMARY KEY (Schl )
);
CREATE TABLE SchoolPerformanceSHUP(
    Schl INT,
    Grade VARCHAR,
    StudentGroupName VARCHAR,
    NScored INT,
    PctAdvanced DECIMAL,
    PctProficient DECIMAL,
    PctBasic DECIMAL,
    PctBelowBasic DECIMAL,
    Growth DECIMAL,
    PRIMARY KEY (Schl )
);
CREATE TABLE PercentLowIncomebySchool(
    SchoolNumber INT,
    Percent DECIMAL,
    PRIMARY KEY (SchoolNumber )
);
CREATE TABLE LowIncomeSchoolsDesignatedforTeacherLoan(
    SchoolNumber INT,
    Percent DECIMAL,
    PRIMARY KEY (SchoolNumber )
);
CREATE TABLE DropOutRates(
    Schl INT,
    Enrollment INT,
    MaleDropouts INT,
    FemaleDropouts INT,
    TotalDropouts INT,
    DropOutRate DECIMAL,
    PRIMARY KEY (Schl )
);
CREATE TABLE PublicDropOutRates(
    Schl INT,
    MaleDropouts INT,
    FemaleDropouts INT,
    TotalDropouts INT,
    DropOutRate DECIMAL,
    PRIMARY KEY (Schl )
);
