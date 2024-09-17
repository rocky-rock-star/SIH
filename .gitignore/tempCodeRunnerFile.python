import sqlite3

EMISSIONS_DB = 'emissions.db'
OFFSETS_DB = 'offsets.db'

def compute_emission_factors():
    # Connect to the emissions database
    conn = sqlite3.connect(EMISSIONS_DB)
    cursor = conn.cursor()

    # SQL query to get average emission_quant and emitter_quant per emitting_activity
    query = '''
    SELECT emitting_activity,
           AVG(emission_quant) AS avg_emission,
           AVG(emitter_quant) AS avg_emitter_quantity
    FROM emissions
    GROUP BY emitting_activity
    '''
    cursor.execute(query)
    results = cursor.fetchall()
    conn.close()

    # Calculate emission factors
    emission_factors = {}
    for emitting_activity, avg_emission, avg_emitter_quantity in results:
        if avg_emitter_quantity != 0:
            emission_factors[emitting_activity] = avg_emission / avg_emitter_quantity
        else:
            emission_factors[emitting_activity] = 0

    return emission_factors

def compute_offset_factors():
    # Connect to the offsets database
    conn = sqlite3.connect(OFFSETS_DB)
    cursor = conn.cursor()

    # SQL query to get average offset values
    query = '''
    SELECT offsetting_activity,
           AVG(offsetting_quant) AS avg_offset_value,
           AVG(offsetter_quant) AS avg_offsetter_value
    FROM offsets
    GROUP BY offsetting_activity
    '''
    cursor.execute(query)
    results = cursor.fetchall()
    conn.close()

    # Process offset factors (if needed)
    offset_factors = {}
    for offsetting_activity, avg_offset_value, avg_offsetter_value in results:
        if avg_offsetter_value != 0:
            offset_factors[offsetting_activity] = avg_offset_value / avg_offsetter_value
        else:
            emission_factors[offsetting_activity] = 0

    return offset_factors

# Compute the factors
emission_factors = compute_emission_factors()
offset_factors = compute_offset_factors()

# For testing purposes, you can print the results
if __name__ == '__main__':
    print("Emission Factors:")
    for activity, factor in emission_factors.items():
        print(f"{activity}: {factor}")

    print("\nOffset Factors:")
    for method, value in offset_factors.items():
        print(f"{method}: {value}")
