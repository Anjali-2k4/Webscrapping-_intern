import requests
from bs4 import BeautifulSoup
import mysql.connector

# Function to scrape HTML table data from the URL
def scrape_html_table(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    table = soup.find('table', {'id': 'customers'})

    data = []
    for row in table.find_all('tr'):
        cols = row.find_all('td')
        cols = [col.text.strip() for col in cols]
        data.append(cols)

    return data[1:]  # Skip the header row

# Function to insert data into MySQL database
def insert_data_into_mysql(data):
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='Anjali@6699',
        database='info'
    )

    cursor = connection.cursor()

    # Create the table if it doesn't exist
    create_table_query = '''
    CREATE TABLE IF NOT EXISTS table_name (
        company VARCHAR(255),
        contact VARCHAR(255),
        country VARCHAR(255)
    )
    '''
    cursor.execute(create_table_query)

    # Insert data into the table
    insert_query = 'INSERT INTO table_name (company, contact, country) VALUES (%s, %s, %s)'
    cursor.executemany(insert_query, data)

    connection.commit()
    cursor.close()
    connection.close()

if __name__ == "__main__":
    url = "https://www.w3schools.com/html/html_tables.asp"
    table_data = scrape_html_table(url)
    insert_data_into_mysql(table_data)
