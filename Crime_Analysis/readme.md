# Crime Analysis and Mapping with Folium

## IDS Assignment - 03

### Abdullah Arif

- **Class:** BS-DS 3A
- **Roll no:** 22L-7764
- **Due date:** 30/11/2023

This repository contains code for an assignment related to crime analysis and mapping using Folium, as part of the IDS course. The primary goal is to analyze a crimes dataset and visualize the results through interactive maps.

### Code Overview

1. **Data Loading and Exploration:**
   - Reads a crimes dataset from a CSV file.
   - Identifies the most frequently committed crime and its category.
   - Calculates ratios, time span, and displays the top 10 offenses.

2. **Distribution of Crimes Across Weekdays:**
   - Determines the most and least common weekdays for crimes.
   - Plots a histogram showing the distribution of crimes across different weekdays.

3. **Geographical Locations with Highest Crime Rate:**
   - Identifies block locations, addresses, and geographical coordinates with the highest crime rates.

4. **Folium Mapping:**
   - Converts the dataset to a GeoDataFrame for spatial analysis.
   - Creates a GeoJSON file and a Folium map displaying crime locations.
   - Utilizes Marker Clusters for better visualization.

### Instructions for Use:

1. **Environment Setup:**
   - Ensure you have the necessary Python libraries installed (NumPy, Pandas, Matplotlib, Seaborn, GeoPandas, Folium).
   - The dataset should be named "crimes_dataset.csv."

2. **Run the Code:**
   - Execute the code in a Python environment (e.g., Jupyter Notebook) to perform crime analysis and generate the Folium map.

3. **Review Results:**
   - Examine the output in the form of printed statistics, visualizations, and an interactive map saved as "crime_map.html."

4. **Additional Files:**
   - The repository includes a GeoJSON file ("crime_data.geojson") generated from the dataset.

### Visualization Screenshots:

1. **Top 10 Offenses Barplot:**
   - A barplot showing the top 10 offenses and their occurrences.

2. **Weekday Crime Distribution:**
   - Histogram illustrating the distribution of crimes across different weekdays.

3. **Interactive Folium Map:**
   - An interactive map with marker clusters representing crime locations.

### Conclusion:

This project provides insights into crime patterns, emphasizing spatial analysis through visualizations. The Folium map offers an interactive experience for exploring crime data geographically.

Feel free to explore the code, run it in your environment, and contribute to further enhancements!
