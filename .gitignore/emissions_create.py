import sqlite3

# Connect to the SQLite3 database (create it if it doesn't exist)
conn = sqlite3.connect('emissions.db')

# Create a cursor object to execute SQL commands
cursor = conn.cursor()

# SQL query to create the table
create_table_query = '''
CREATE TABLE IF NOT EXISTS emissions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    emitting_activity TEXT NOT NULL,
    emitter_quant REAL,
    emission_quant REAL NOT NULL,
    datasource TEXT NOT NULL
);
'''

# Execute the SQL query to create the table
cursor.execute(create_table_query)

# Commit the changes
conn.commit()

# Close the connection
conn.close()
