# the file from which the webapp will run

from flask import Flask, request, render_template #import stuff needed for the webapp
from compute_factors import emission_factors, offset_factors #import values computed from the dummy databases

app = Flask(__name__)

def get_activity_emission(coal_extracted, kms_traveled, kwh_used): #create dictionary to store activity wise emissions
    emissions_dict = {
        'coal': coal_extracted * emission_factors['Mining'],
        'travel': kms_traveled * emission_factors['Transport'],
        'kwh': kwh_used * emission_factors['Machinery Operation']
    }
    return emissions_dict

def get_total(dictionary): #func to find total emissions
    return sum(dictionary.values())

def calculate_offsets(total_emission): #func to calculate req units in offset techniques for carbon neutrality
    offsets_needed = {}
    for method, offset_value in offset_factors.items():
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
    activity_emissions = get_activity_emission(coal_extracted, kilometers_traveled, energy_used)
    #find total emissions from the activity emisions
    total_emission = get_total(activity_emissions)
    #find offset suggestions
    offset_needed = calculate_offsets(total_emission)

    #plug in values to be displayed in the result webpage
    return render_template('result1.html', emission=activity_emissions, total=total_emission, offsets=offset_needed)


if __name__ == '__main__':
    app.run(debug=True)
    