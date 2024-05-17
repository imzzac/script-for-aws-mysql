import mysql.connector

# Configure database connection
db_config = {
    'user': 'root',
    'password': '',  # replace 'your_password' with your actual MySQL root password
    'host': '127.0.0.1',
    'database': 'company'
}

# Establish a database connection
conn = mysql.connector.connect(**db_config)

# Create a cursor object
cursor = conn.cursor()

# Define the query
query = "SELECT * FROM employees"

# Execute the query
cursor.execute(query)

# Fetch all the rows
rows = cursor.fetchall()

# Print the results
print("ID | Name  | Salary")
print("---|-------|---------")
for row in rows:
    print(f"{row[0]} | {row[1]} | {row[2]}")

# Close the cursor and connection
cursor.close()
conn.close()
