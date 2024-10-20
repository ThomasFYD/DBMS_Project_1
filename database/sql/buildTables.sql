CREATE TABLE SchoolData (
    DistrictName VARCHAR(50),
    Name VARCHAR(50),
    AUN INT PRIMARY KEY AUTO_INCREMENT,
    Schl INT NOT NULL,
    SchoolName VARCHAR(50),
    SchoolAddressStreet VARCHAR(50),
    SchoolAddressCity VARCHAR(50),
    SchoolAddressState VARCHAR(50),
    SchoolZipCode VARCHAR(50),
    Website VARCHAR(50),
    TelephoneNumber VARCHAR(50),
    GradesOffered VARCHAR(50),
    TitleISchool VARCHAR(50),
    SchoolEnrollment INT,
    PercentGiftedStudents DECIMAL,
    IntermediateUnitName VARCHAR(50),
    IntermediateUnitWebsite VARCHAR(50),
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
    MilitaryConnected DECIMAL
);

CREATE TABLE SchoolPerformanceE(
    Schl INT PRIMARY KEY,
    Grade INT,
    StudentGroupName VARCHAR(50),
    NScored INT,
    PctAdvanced DECIMAL,
    PctProficient DECIMAL,
    PctBasic DECIMAL,
    PctBelowBasic DECIMAL,
    Growth DECIMAL,
    FOREIGN KEY (Schl) REFERENCES SchoolData(Schl) ON DELETE CASCADE
);

CREATE TABLE SchoolPerformanceEHUP(
    Schl INT PRIMARY KEY,
    Grade VARCHAR(50),
    StudentGroupName VARCHAR(50),
    NScored INT,
    PctAdvanced DECIMAL,
    PctProficient DECIMAL,
    PctBasic DECIMAL,
    PctBelowBasic DECIMAL,
    Growth DECIMAL,
    FOREIGN KEY (Schl) REFERENCES SchoolData(Schl) ON DELETE CASCADE
);

CREATE TABLE SchoolPerformanceM(
    Schl INT PRIMARY KEY,
    Grade VARCHAR(50),
    StudentGroupName VARCHAR(50),
    NScored INT,
    PctAdvanced DECIMAL,
    PctProficient DECIMAL,
    PctBasic DECIMAL,
    PctBelowBasic DECIMAL,
    Growth DECIMAL,
    FOREIGN KEY (Schl) REFERENCES SchoolData(Schl) ON DELETE CASCADE
);

CREATE TABLE SchoolPerformanceMHUP(
    Schl INT PRIMARY KEY,
    Grade VARCHAR(50),
    StudentGroupName VARCHAR(50),
    NScored INT,
    PctAdvanced DECIMAL,
    PctProficient DECIMAL,
    PctBasic DECIMAL,
    PctBelowBasic DECIMAL,
    Growth DECIMAL,
    FOREIGN KEY (Schl) REFERENCES SchoolData(Schl) ON DELETE CASCADE
);

CREATE TABLE SchoolPerformanceS(
    Schl INT PRIMARY KEY,
    Grade VARCHAR(50),
    StudentGroupName VARCHAR(50),
    NScored INT,
    PctAdvanced DECIMAL,
    PctProficient DECIMAL,
    PctBasic DECIMAL,
    PctBelowBasic DECIMAL,
    Growth DECIMAL,
    FOREIGN KEY (Schl) REFERENCES SchoolData(Schl) ON DELETE CASCADE
);

CREATE TABLE SchoolPerformanceSHUP(
    Schl INT PRIMARY KEY,
    Grade VARCHAR(50),
    StudentGroupName VARCHAR(50),
    NScored INT,
    PctAdvanced DECIMAL,
    PctProficient DECIMAL,
    PctBasic DECIMAL,
    PctBelowBasic DECIMAL,
    Growth DECIMAL,
    FOREIGN KEY (Schl) REFERENCES SchoolData(Schl) ON DELETE CASCADE
);

CREATE TABLE PercentLowIncomebySchool(
    SchoolNumber INT PRIMARY KEY AUTO_INCREMENT,
    Percent DECIMAL,
    FOREIGN KEY (SchoolNumber) REFERENCES SchoolData(Schl) ON DELETE CASCADE
);

CREATE TABLE LowIncomeSchoolsDesignatedforTeacherLoan(
    SchoolNumber INT PRIMARY KEY AUTO_INCREMENT,
    Percent DECIMAL,
    FOREIGN KEY (SchoolNumber) REFERENCES SchoolData(Schl) ON DELETE CASCADE
);

CREATE TABLE DropOutRates(
    Schl INT PRIMARY KEY,
    Enrollment INT,
    MaleDropouts INT,
    FemaleDropouts INT,
    TotalDropouts INT,
    DropOutRate DECIMAL,
    FOREIGN KEY (Schl) REFERENCES SchoolData(Schl) ON DELETE CASCADE
);
