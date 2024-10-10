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

# Function to convert CSV data to a MySQL table
def csv_to_mysql(file_path, table_name, connection):
    # Read the CSV file into a pandas DataFrame
    df = pd.read_csv(file_path)

    # Create a cursor object
    cursor = connection.cursor()

    # Extract column names and prepare column definitions
    columns = df.columns.tolist()
    column_definitions = ', '.join([f'{col} VARCHAR(255)' for col in columns])

    # Dynamically create the CREATE TABLE query
    create_table_query = f"CREATE TABLE IF NOT EXISTS {table_name} ({column_definitions})"
    
    # Execute the CREATE TABLE query
    cursor.execute(create_table_query)

    # Insert data into the table row by row
    for index, row in df.iterrows():
        values = tuple(row)
        placeholders = ', '.join(['%s'] * len(values))
        insert_query = f"INSERT INTO {table_name} VALUES ({placeholders})"
        cursor.execute(insert_query, values)

    # Commit the transaction
    connection.commit()

    # Close the cursor and connection
    cursor.close()

# Example usage
if __name__ == "__main__":
    # MySQL database credentials
    mysql_host = "localhost"
    mysql_user = "your_username"
    mysql_password = "your_password"
    mysql_database = "your_database"
    table_name = "your_table_name"
    csv_file_path = "path_to_your_csv_file.csv"

    # Create a connection to the MySQL database
    connection = create_mysql_connection(mysql_host, mysql_user, mysql_password, mysql_database)

    # Convert the CSV file to a MySQL table
    csv_to_mysql(csv_file_path, table_name, connection)

    # Close the MySQL connection
    connection.close()
