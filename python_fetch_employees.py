from flask import Flask, render_template_string
import mysql.connector

app = Flask(__name__)

# Configure database connection
db_config = {
    'user': 'root',
    'password': 'your_password',  # replace 'your_password' with your actual MySQL root password
    'host': '10.0.0.135',
    'database': 'company'
}

@app.route('/')
def index():
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

    # Close the cursor and connection
    cursor.close()
    conn.close()

    # HTML template
    html = """
    <!doctype html>
    <html>
    <head>
        <title>Employee Salaries</title>
    </head>
    <body>
        <h1>Employee Salaries</h1>
        <table border="1">
            <tr>
                <th>ID</th>
                <th>Name</th>
                <th>Salary</th>
            </tr>
            {% for row in rows %}
            <tr>
                <td>{{ row[0] }}</td>
                <td>{{ row[1] }}</td>
                <td>{{ row[2] }}</td>
            </tr>
            {% endfor %}
        </table>
    </body>
    </html>
    """
    
    return render_template_string(html, rows=rows)

if __name__ == '__main__':
    app.run(debug=True)
