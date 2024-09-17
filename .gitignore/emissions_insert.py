import sqlite3

# Connect to the SQLite3 database
conn = sqlite3.connect('emissions.db')

# Create a cursor object to execute SQL commands
cursor = conn.cursor()

# SQL query to insert values into the table
insert_values_query = '''
INSERT INTO emissions (emitting_activity, emitter_quant, emission_quant, datasource)
VALUES (?, ?, ?, ?)
'''

values = [
    ('Mining', 1000, 300, 'Dummy'),
    ('Mining', 2500, 600, 'Dummy'),
    ('Transport', 1500, 200, 'Dummy'),
    ('Machinery Operation', 2000, 1640, 'Dummy'),
    ('Machinery Operation', 1800, 1500, 'Dummy')
]

# Execute the SQL query with the example data
cursor.executemany(insert_values_query, values)

# Commit the changes
conn.commit()

# Close the connection
conn.close()
