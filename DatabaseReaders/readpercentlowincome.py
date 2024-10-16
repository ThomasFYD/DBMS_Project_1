import sqlite3
import csv

# Connect to the SQLite database
conn = sqlite3.connect('schoolFacts.sqlite')
cursor = conn.cursor()


# Insert data function with REPLACE to update duplicates
def insert_data(school_number, percent):
    sql = '''INSERT OR REPLACE INTO LowIncomeSchoolsDesignatedforTeacherLoan (SchoolNumber, Percent)
             VALUES (?, ?)'''
    cursor.execute(sql, (school_number, percent))
    conn.commit()

# Process the CSV and insert data into the table
def process_csv(file_name):
    with open(file_name, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header row
        next(reader)
        for row in reader:
            school_number = (row[0])  # School Number
            percent = float(row[4])      # Percent
            insert_data(school_number, percent)

# Call the function to process your CSV file
process_csv('/Users/isaac/CLionProjects/DBMS_Project_1/database/csv/loanCancellations.csv')

# Close the database connection
conn.close()