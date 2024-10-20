CREATE TABLE SchoolData (
    DistrictName VARCHAR(150),
    Name VARCHAR(150),
    AUN INT PRIMARY KEY AUTO_INCREMENT,
    Schl INT NOT NULL,
    SchoolName VARCHAR(150),
    SchoolAddressStreet VARCHAR(150),
    SchoolAddressCity VARCHAR(150),
    SchoolAddressState VARCHAR(150),
    SchoolZipCode VARCHAR(150),
    Website VARCHAR(150),
    TelephoneNumber VARCHAR(150),
    GradesOffered VARCHAR(150),
    TitleISchool VARCHAR(150),
    SchoolEnrollment INT,
    PercentGiftedStudents DECIMAL,
    IntermediateUnitName VARCHAR(150),
    IntermediateUnitWebsite VARCHAR(150),
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
    StudentGroupName VARCHAR(150),
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
    Grade VARCHAR(150),
    StudentGroupName VARCHAR(150),
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
    Grade VARCHAR(150),
    StudentGroupName VARCHAR(150),
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
    Grade VARCHAR(150),
    StudentGroupName VARCHAR(150),
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
    Grade VARCHAR(150),
    StudentGroupName VARCHAR(150),
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
    Grade VARCHAR(150),
    StudentGroupName VARCHAR(150),
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
