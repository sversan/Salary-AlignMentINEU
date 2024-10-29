from flask import Flask, render_template
import pandas as pd

import jinja2
env = jinja2.Environment()
env.globals.update(zip=zip)

app = Flask(__name__)

# Sample data: Country and average salary (in Euros)
data = {
    'Country': ['Germany', 'France', 'Italy', 'Spain', 'Poland', 'Sweden', 'Netherlands', 'Denmark','Romania'],
    'Average Salary': [40000, 35000, 30000, 28000, 25000, 42000, 45000, 48000,9450]
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Function to assign colors based on salary
def assign_color(salary):
    if salary >= 45000:
        return 'green'
    elif salary >= 35000:
        return 'blue'
    elif salary >= 25000:
        return 'orange'
    else:
        return 'red'

# Assign colors to each country
df['Color'] = df['Average Salary'].apply(assign_color)

@app.route('/')
def index():
    countries = df['Country'].tolist()
    salaries = df['Average Salary'].tolist()
    colors = df['Color'].tolist()
    
    # Ensure zip is defined correctly in the template rendering context
    return render_template('index.html', countries=countries, salaries=salaries, colors=colors,zip=zip)

if __name__ == '__main__':
    app.run(debug=True)
