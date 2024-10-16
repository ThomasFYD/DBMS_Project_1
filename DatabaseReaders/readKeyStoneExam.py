import sqlite3
import csv

# Connect to the SQLite database
conn = sqlite3.connect('schoolFacts.sqlite')
cursor = conn.cursor()

# Insert data function
def insert_data(table, data):
    sql = f'''INSERT INTO {table} 
            (Schl, Grade, StudentGroupName, NScored, PctAdvanced, PctProficient, PctBasic, PctBelowBasic, Growth)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)'''
    cursor.execute(sql, data)
    conn.commit()

def is_unique_schl(schl):
    query = '''
    SELECT Schl FROM SchoolPerformanceE UNION 
    SELECT Schl FROM SchoolPerformanceM UNION 
    SELECT Schl FROM SchoolPerformanceS 
    UNION 
    SELECT Schl FROM SchoolPerformanceEHUP UNION 
    SELECT Schl FROM SchoolPerformanceMHUP UNION 
    SELECT Schl FROM SchoolPerformanceSHUP
    '''
    cursor.execute(query)
    existing_schls = {row[0] for row in cursor.fetchall()}
    return schl not in existing_schls

# Process the CSV and insert data into the appropriate table
def process_csv(file_name):
    with open(file_name, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header row
        
        for row in reader:
            Schl = int(row[0])
            district_name = row[1]
            school_name = row[2]
            subject = row[3]  # E, M, S
            grade = row[4]
            student_group_name = row[5]
            NScored = int(row[6]) if row[6] != 'IS' else None
            PctAdvanced = (row[7]) if row[7] != 'IS' else None
            PctProficient = (row[8]) if row[8] != 'IS' else None
            PctBasic = (row[9]) if row[9] != 'IS' else None
            PctBelowBasic = (row[10]) if row[10] != 'IS' else None
            Growth = (row[11]) if row[11] != 'IS' else None
            
            # Determine the table based on subject and student group name
            if subject == 'E':
                if 'Historically Underperforming' in student_group_name:
                    table = 'SchoolPerformanceEHUP'
                else:
                    table = 'SchoolPerformanceE'
            elif subject == 'M':
                if 'Historically Underperforming' in student_group_name:
                    table = 'SchoolPerformanceMHUP'
                else:
                    table = 'SchoolPerformanceM'
            elif subject == 'S':
                if 'Historically Underperforming' in student_group_name:
                    table = 'SchoolPerformanceSHUP'
                else:
                    table = 'SchoolPerformanceS'
            
            # Insert the data into the appropriate table
            if is_unique_schl(Schl):
                data = (Schl, grade, student_group_name, NScored, PctAdvanced, PctProficient, PctBasic, PctBelowBasic, Growth)
                insert_data(table, data)
            else:
                print(f"Duplicate Schl value found: {Schl}. Skipping insertion.")

# Call the function to process your CSV file
process_csv('/Users/isaac/CLionProjects/DBMS_Project_1/database/csv/keystoneExam.csv')

# Close the database connection
conn.close()