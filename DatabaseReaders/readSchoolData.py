import pandas as pd
import sqlite3

# Function to establish a connection to SQLite
def create_sqlite_connection(db_file):
    conn = sqlite3.connect(db_file)
    return conn

# Function to read CSV, pivot the data, and insert it into an SQLite database
def csv_to_sqlite_school_data(file_path, connection):
    # Read the CSV file into a pandas DataFrame
    df = pd.read_csv(file_path)
    
    # Pivot the data to make DataElement as columns and DisplayValue as values
    df_pivot = df.pivot_table(index=["DistrictName", "Schl", "AUN"], 
                              columns="DataElement", 
                              values="DisplayValue", 
                              aggfunc='first').reset_index()
    # Insert data into the SchoolData table
    insert_query = """
    INSERT INTO SchoolData (
        DistrictName ,Schl, AUN, SchoolName, SchoolAddressStreet, SchoolAddressCity,
        SchoolAddressState, SchoolZipCode, Website, TelephoneNumber, GradesOffered,
        TitleISchool, SchoolEnrollment, PercentGiftedStudents, IntermediateUnitName, IntermediateUnitWebsite,
        AmericanIndianAlaskanNative, Asian, BlackAfricanAmerican, Hispanic, TwoOrMoreRaces, White,
        NativeHawaiianPacificIslander, EconomicallyDisadvantaged, EnglishLearner, SpecialEducation,
        FemaleSchool, MaleSchool, FosterCare, Homeless, MilitaryConnected
    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,?)
    ON CONFLICT(AUN) DO NOTHING;  -- Avoids inserting duplicates based on AUN
    """

    # Iterate over the pivoted DataFrame and insert each row into the SQLite table
    for index, row in df_pivot.iterrows():
        connection.execute(insert_query, (
            row['DistrictName'], row['Schl'], row['AUN'], row.get('School Name', None), 
            row.get('School Address (Street)', None), row.get('School Address (City)', None), 
            row.get('School Address (State)', None), row.get('School Zip Code', None), row.get('Website', None), 
            row.get('Telephone Number', None), row.get('Grades Offered', None), 
            row.get('Title I School', None), row.get('School Enrollment', None), 
            row.get('Percent of Gifted Students', None), row.get('Intermediate Unit Name', None), 
            row.get('Intermediate Unit Website', None), row.get('American Indian/Alaskan Native ', None), 
            row.get('Asian ', None), row.get('Black/African American ', None), row.get('Hispanic ', None), 
            row.get('2 or More Races', None), row.get('White ', None), 
            row.get('Native Hawaiian or other Pacific Islander ', None), 
            row.get('Economically Disadvantaged', None), row.get('English Learner', None), 
            row.get('Special Education', None), row.get('Female (School)', None), 
            row.get('Male (School)', None), row.get('Foster Care', None), 
            row.get('Homeless', None), row.get('Military Connected', None)
        ))

    # Commit the transaction
    connection.commit()

# Example usage
if __name__ == "__main__":
    # Path to your SQLite database file (this will create a new database if it doesn't exist)
    sqlite_db_file = "schoolFacts.sqlite"
    
    # Path to your CSV file
    csv_file_path = "/Users/isaac/CLionProjects/DBMS_Project_1/database/csv/SchoolFastFacts_20182019.csv"

    # Establish a connection to the SQLite database
    connection = create_sqlite_connection(sqlite_db_file)

    # Load the data from the CSV file into the SchoolData table
    csv_to_sqlite_school_data(csv_file_path, connection)

    # Close the database connection
    connection.close()