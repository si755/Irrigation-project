# Data Preprocessing (`data_preprocessing.py`)

import pandas as pd

# Load sample survey data
data = pd.read_csv('data/sample_survey_data.csv')

# Clean and preprocess data
data.dropna(inplace=True)
data['Efficiency'] = data['Water_Used'] / data['Area_Irrigated']

# Save cleaned data
data.to_csv('data/cleaned_survey_data.csv', index=False)
print("Data preprocessing complete. Cleaned data saved!")

import geopandas as gpd
import matplotlib.pyplot as plt

# Load GIS data
gis_data = gpd.read_file('data/gis_layer_sample.geojson')

# Plot irrigation infrastructure
gis_data.plot(column='Efficiency', cmap='Blues', legend=True)
plt.title('Irrigation Efficiency Map')
plt.savefig('visualizations/irrigation_efficiency_map.png')
plt.show()

import pandas as pd

# Load cleaned data
data = pd.read_csv('data/cleaned_survey_data.csv')

# Generate a summary report
summary = data.groupby('Region')['Efficiency'].mean().reset_index()
summary.to_excel('docs/progress_report_sample.xlsx', index=False)
print("Progress report generated!")
