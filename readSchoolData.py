import pandas as pd
import mysql.connector

# Function to create a MySQL connection
def create_mysql_connection(host, user, password, database):
    return mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database
    )

# Function to insert data from CSV into the SchoolData table
def csv_to_mysql_school_data(file_path, connection):
    # Read the CSV file into a pandas DataFrame
    df = pd.read_csv(file_path)

    # Create a cursor object
    cursor = connection.cursor()

    # Prepare the SQL INSERT query template
    insert_query = '''
    INSERT INTO SchoolData (
        DistrictName, Name, AUN, Schl, DataElement, DisplayValue,
        SchoolName, SchoolAddressStreet, SchoolAddressCity, SchoolAddressState, 
        SchoolZipCode, Website, TelephoneNumber, GradesOffered, TitleISchool, 
        SchoolEnrollment, PercentGiftedStudents, IntermediateUnitName, IntermediateUnitWebsite,
        AmericanIndianAlaskanNative, Asian, BlackAfricanAmerican, Hispanic, TwoOrMoreRaces,
        White, NativeHawaiianPacificIslander, EconomicallyDisadvantaged, EnglishLearner,
        SpecialEducation, FemaleSchool, MaleSchool, FosterCare, Homeless, MilitaryConnected
    ) 
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    '''

    # Loop through the DataFrame rows and insert data into the MySQL table
    for index, row in df.iterrows():
        cursor.execute(insert_query, (
            row['DistrictName'], row['Name'], row['AUN'], row['Schl'], row['DataElement'], row['DisplayValue'],
            row['School Name'], row['School Address (Street)'], row['School Address (City)'], row['School Address (State)'], 
            row['School Zip Code'], row['Website'], row['Telephone Number'], row['Grades Offered'], row['Title I School'], 
            row['School Enrollment'], row['Percent of Gifted Students'], row['Intermediate Unit Name'], row['Intermediate Unit Website'],
            row['American Indian/Alaskan Native'], row['Asian'], row['Black/African American'], row['Hispanic'], row['2 or More Races'],
            row['White'], row['Native Hawaiian or other Pacific Islander'], row['Economically Disadvantaged'], row['English Learner'],
            row['Special Education'], row['Female (School)'], row['Male (School)'], row['Foster Care'], row['Homeless'], row['Military Connected']
        ))

    # Commit the transaction
    connection.commit()

    # Close the cursor
    cursor.close()

# Example usage
if __name__ == "__main__":
    # MySQL database credentials
    mysql_host = "localhost"
    mysql_user = "your_username"
    mysql_password = "your_password"
    mysql_database = "your_database"
    
    # CSV file path
    csv_file_path = "path_to_your_csv_file.csv"

    # Create a connection to the MySQL database
    connection = create_mysql_connection(mysql_host, mysql_user, mysql_password, mysql_database)

    # Insert the CSV data into the SchoolData table
    csv_to_mysql_school_data(csv_file_path, connection)

    # Close the MySQL connection
    connection.close()
