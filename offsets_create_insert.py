import sqlite3

# Connect to the SQLite3 database (create it if it doesn't exist)
conn = sqlite3.connect('offsets.db')

# Create a cursor object to execute SQL commands
cursor = conn.cursor()

# SQL query to create the table if it doesn't already exist
create_table_query = '''
CREATE TABLE IF NOT EXISTS offsets (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    offsetting_activity TEXT NOT NULL,
    offsetter_quant REAL NOT NULL,
    offsetting_quant REAL NOT NULL,
    datasource TEXT NOT NULL
);
'''

# Execute the SQL query to create the table
cursor.execute(create_table_query)

# SQL query to insert values into the table
insert_values_query = '''
INSERT INTO offsets (offsetting_activity, offsetter_quant, offsetting_quant, datasource)
VALUES (?, ?, ?, ?)
'''

# Example data to insert
values = [
    ('Afforestation', 1000, 2500, 'Dummy'),
    ('Solar Farms', 500, 1500, 'Dummy'),
    ('Wind Farms', 200, 800, 'Dummy'),
    ('Biomass energy', 500, 1500, 'Dummy'),
    ('Carbon capture and storage', 200, 800, 'Dummy')
]

# Execute the SQL query with the example data
cursor.executemany(insert_values_query, values)

# Commit the changes
conn.commit()

# Close the connection
conn.close()
