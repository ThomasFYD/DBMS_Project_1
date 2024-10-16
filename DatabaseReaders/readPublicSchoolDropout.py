import sqlite3
import csv

# Connect to the SQLite database
conn = sqlite3.connect('schoolFacts.sqlite')
cursor = conn.cursor()



# Insert data function
def insert_data(schl, male_dropouts, female_dropouts, total_dropouts, dropout_rate):
    sql = '''INSERT OR REPLACE INTO PublicDropOutRates (Schl, MaleDropouts, FemaleDropouts, TotalDropouts, DropOutRate)
             VALUES (?, ?, ?, ?, ?)'''
    cursor.execute(sql, (schl, male_dropouts, female_dropouts, total_dropouts, dropout_rate))
    conn.commit()

# Function to process the CSV file and insert data into the table
def process_csv(file_name):
    with open(file_name, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header row
        
        for row in reader:
            schl = (row[1])  # School number (AUN)
            # Remove commas from Enrollment and convert to int
            try:
                male_dropouts = int(row[6].replace(",", ""))  # Remove commas and convert to int
            except ValueError:
                male_dropouts = int(row[6])
                continue
            try:
                female_dropouts = int(row[7].replace(",", ""))  # Remove commas and convert to int
            except ValueError:
                female_dropouts = int(row[7])
                continue
            try:
                total_dropouts = int(row[8].replace(",", ""))  # Remove commas and convert to int
            except ValueError:
                total_dropouts = int(row[8])
                continue
            # Convert dropout rate to float (strip % and divide by 100)
            dropout_rate = float(row[7].strip('%')) / 100
            
            # Insert data into the table
            insert_data(schl, male_dropouts, female_dropouts, total_dropouts, dropout_rate)

# Call the function to process your CSV file
process_csv('/Users/isaac/CLionProjects/DBMS_Project_1/database/csv/publicschoolDropoutRate.csv')

# Close the database connection
conn.close()