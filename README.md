# Sea-Level-Predictor
Sea Level Predictor Python Data Analysis Project

A Python-based data analysis and visualization project that examines sea level changes over time and predicts future trends using linear regression. This project leverages historical data from the NOAA (National Oceanic and Atmospheric Administration) and uses matplotlib, pandas, and scipy for data visualization and prediction modeling.

Dependencies:

pandas

matplotlib

scipy

numpy (optional)

pytest (for testing

Dataset
The dataset epa-sea-level.csv includes historical data on global sea levels collected by NOAA. Key columns:

Year: The year of the measurement

CSIRO Adjusted Sea Level: Sea level in inches, adjusted for seasonal and measurement bias

Project Goals
Visualize historical sea level data

Fit a linear regression line to the full dataset

Fit a second regression line using data from year 2000 onward

Extend both lines to the year 2050 to visualize predicted sea level rise
Output
The script creates a plot:

Scatter plot of actual sea level data

Regression line (all years)

Regression line (from year 2000)

Projection to 2050

Technical Highlights
Used SciPy’s linregress for linear regression modeling

Created predictions using slope/intercept from regression

Added regression line from 2000 onward to show modern trends

Used matplotlib to generate and customize plots
