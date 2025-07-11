import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Load data
    df = pd.read_csv('epa-sea-level.csv')

    # Scatter plot
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])

    # Line of best fit using all data
    fit_all = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    plt.plot(df['Year'], fit_all.intercept + fit_all.slope * df['Year'], label='Fit all data', color='red')

    # Line of best fit using data from 2000 onward
    df_recent = df[df['Year'] >= 2000]
    fit_recent = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
    plt.plot(df_recent['Year'], fit_recent.intercept + fit_recent.slope * df_recent['Year'], label='Fit from 2000', color='green')

    # Labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    plt.legend()

    # Save and return the plot
    plt.savefig('sea_level_plot.png')
    return plt.gcf()
