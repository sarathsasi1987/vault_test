from flask import Flask
from flask import render_template
import mysql.connector
import os

app = Flask(__name__)

@app.route('/')
def display_data():
    # Retrieve secrets from the environment
    db_host = os.environ.get("DB_HOST")
    db_user = os.environ.get("DB_USER")
    db_password = os.environ.get("DB_PASSWORD")
    db_database = os.environ.get("DB_DATABASE")

    # Connect to the MySQL database using the retrieved secrets
    connection = mysql.connector.connect(
        host=db_host,
        user=db_user,
        password=db_password,
        database=db_database
    )

    cursor = connection.cursor()

    # Query the database
    cursor.execute('SELECT * FROM ci_cd_popularity')
    data = cursor.fetchall()

    # Close the database connection
    cursor.close()
    connection.close()

    return render_template('./index.html', data=data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
