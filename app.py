# this is the primary development file

from flask import Flask, request, render_template

app = Flask(__name__)

#arbitrary values for emissions factors, to be replaced by a dbms reading func
EMISSION_FACTORS = {
    'coal': 2.5,            
    'kilometers': 0.3,      
    'energy': 0.5           
}

#arbitrary offset factors, to be replaced with a dbms func
OFFSET_VALUES = {
    'Afforestation': 1000,  
    'Solar Farms': 800,
    'Wind Farms': 600,
    'Carbon Capture and Storage': 1200,
    'Biomass Energy': 1500
}

def activity_emission(activity, emission_factor): #func to find activity wise emissions
    emission = activity*emission_factor
    return emission 

def get_total(a1, a2, a3): #func to find total emissions
    total = a1+a2+a3
    return total

def calculate_offsets(total_emission): #func to calculate req units in offset techniques
    offsets_needed = {}
    for method, offset_value in OFFSET_VALUES.items():
        units_needed = total_emission / offset_value
        offsets_needed[method] = units_needed
    return offsets_needed

# Route to display the form as the homepage
@app.route('/')
def index():
    return render_template('index2.html')

#rouite to take values in from the form and process
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
    #find total emissions from the activity emisions
    total_emission = get_total(coal_emission, transport_emission, energy_emission)
    #find offset suggestions
    offset_needed = calculate_offsets(total_emission)

    #plug in values to be displayed in the result webpage
    #link to result.html for list view of offsets and result1 for table view of offsets
    return render_template('result1.html', coal=coal_emission, transport=transport_emission, energy=energy_emission, total=total_emission, offsets=offset_needed)
    


    #in case we wanna try to display form and result on the same page, keep commented unless required
    #return render_template('index2.html', coal=coal_emission, transport=transport_emission, energy=energy_emission, total=total_emission)

if __name__ == '__main__':
    app.run(debug=True)
    