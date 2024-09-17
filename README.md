# Coal mines emissions and Offsets Calculator Web App

This web application allows coal companies to calculate their total carbon emissions based on data they input, including the amount of coal extracted, kilometers traveled for transportation, and kilowatt-hours (kWh) used for machinery operations. The app also provides a breakdown of how many units of popular carbon offset methods are required to achieve carbon neutrality.

## Features

- **User Input Form**: Users enter data on coal extraction, transportation distance, and machinery energy use.
- **Emissions Calculation**: The app calculates the total emissions for each activity using database-driven emission factors (current implementation uses dummy data as the data collection process requires time and attention).
- **Carbon Offsetting**: The app calculates how many units of different carbon offset methods are needed to neutralize the total emissions.
- **Results Page**: Displays the total emissions and the required offset units, on a separate results page.

## Technologies Used

- **Backend**: Python (Flask Framework)
- **Database**: SQLite3
- **Frontend**: HTML5, CSS3
- **Deployment**: Flask’s development server (can be deployed to platforms like Heroku or PythonAnywhere)

## Folder Structure

```
project-root/
│
├── app.py               # Main Flask app file
├── compute_factors.py   # File that calculates emission and offset factors
├── emissions.db         # SQLite database storing emissions data
├── offsets.db           # SQLite database storing emissions data
├── templates/
│   ├── index2.html       # HTML form page for input
│   └── results1.html     # HTML results page to display the calculated data
├── static/
│   └── styles.css       # Stylesheet for the HTML pages
└── README.md            # This README file
```

## Getting Started

### Prerequisites

- Python 3.x installed
- Flask installed (`pip install flask`)
- SQLite3 installed (typically included with Python)
- Note: All of these should come out of the box with the .venv directory in the github repository if you are using VS code, else you may need to install Python, flask and SQLite3.

### Setup

1. **Clone the repository or download the folder provided**:
   ```bash
   git clone https://github.com/rocky-rock-star/SIH_Coal_Emission_Calculator.git
   cd SIH_Coal_Emission_Calculator
   ```

2. **Install dependencies**:
- Download and install python and add it to PATH
- Then enter the following command into the terminal
   ```bash
   pip install Flask
   ```

3. **Run the Flask application**:
   ```bash
   python app.py
   ```

4. **Access the application**:
   Open your web browser and go to `http://127.0.0.1:5000/` to access the webapp.


## Application Workflow

1. **Input Form**: Users fill out the form with the following fields:
   - Coal extracted (in tons)
   - Kilometers traveled (in km)
   - Energy used by machinery (in kWh)

2. **Emissions Calculation**: After submission, the backend:
   - Retrieves emission factors from the `compute_factors.py` file or the database.
   - Multiplies the input values by the respective emission factors to calculate the total emissions for each activity.

3. **Carbon Offsetting**: The app calculates how many units of popular offset methods (like planting trees, carbon capture) are needed based on the total emissions.

4. **Results Display**: The app displays the calculated emissions and offsets on a separate results page or the same page as the form.

## Future Features

- **User Accounts**: Allow companies to log in and track their emissions history.
- **API Integration**: Fetch real-time emission factors or offset data from external APIs.
- **Advanced Offsetting Options**: Provide more detailed offsetting options (e.g., different tree species, carbon capture technologies).