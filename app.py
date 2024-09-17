# this is the primary development file

from flask import Flask, request, render_template

app = Flask(__name__)

# Define arbitrary emission factors for each activity
EMISSION_FACTORS = {
    'coal': 2.5,            # kg CO2 per ton of coal extracted
    'kilometers': 0.3,      # kg CO2 per km of transport
    'energy': 0.5           # kg CO2 per kWh of energy used
}

def activity_emission(activity, emission_factor):
    emission = activity*emission_factor
    return emission 

def get_total(a1, a2, a3):
    total = a1+a2+a3
    return total

# Route to display the form (homepage)
@app.route('/')
def index():
    return render_template('index2.html')

@app.route('/submit', methods=['POST'])
def calculate_emissions():
    # Get data from HTML form
    coal_extracted = float(request.form['coal'])
    kilometers_traveled = float(request.form['transport'])
    energy_used = float(request.form['power'])

    # Calculate emissions for each activity
    coal_emission = activity_emission(coal_extracted, EMISSION_FACTORS['coal'])
    transport_emission = activity_emission(kilometers_traveled, EMISSION_FACTORS['kilometers'])
    energy_emission = activity_emission(energy_used, EMISSION_FACTORS['energy'])
    
    total_emission = get_total(coal_emission, transport_emission, energy_emission)

    return render_template('result.html', coal=coal_emission, transport=transport_emission, energy=energy_emission, total=total_emission)
    

    # You can return the total emissions to the frontend (HTML page)
    #return render_template('index2.html', coal=coal_emission, transport=transport_emission, energy=energy_emission, total=total_emission)

if __name__ == '__main__':
    app.run(debug=True)
    