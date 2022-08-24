# MAST30034 Project 1
- Name: Haiyang(Henry) Huang
- Student ID: 1071147


# Information about this Project

**Research Goal:** The Effect of Weather, Population, and Property Price on the Demand for Yellow Taxis in New York City

**Timeline:** 2019 whole year.

# Dataset

TLC trip record data: https://www1.nyc.gov/site/tlc/about/tlc-trip-record-data.page <br />
New York City Population By Neighborhood Tabulation Areas: https://data.cityofnewyork.us/City-Government/New-York-City-Population-By-Neighborhood-Tabulatio/swpk-hqdp <br />
Annualized Sales Update: https://www1.nyc.gov/site/finance/taxes/property-annualized-sales-update.page <br />
New York City Weather: https://www.visualcrossing.com/weather/weather-data-services <br />

# How to use this Repository

To run the pipeline, please visit the `scripts` directory and run the files in order:
1. `Download.ipynb`: This will run 'Download.py' and downloads the raw data into the `data/raw` directory.
2. `Preprocess_part_1.ipynb`: This notebook details all preprocessing steps for TLC taxi dataset and outputs it to the `data/curated` directory.
3. `Preprocess_part_2.ipynb`: This notebook details all preprocessing steps for Weather, Population, and Property Price dataset and outputs it to the `data/curated` directory.
4. `Visualisation.ipynb`: This notebook is used to produce useful graph for analysis on the curated data.
5. `Statistical_Modelling.ipynb`: This notebook is used for modelling.

# Some code reference
Use of folium: https://towardsdatascience.com/folium-and-choropleth-map-from-zero-to-pro-6127f9e68564 <br />
Use of Spark/statsmodel/geopands/folium: MAST30034 Tutorial (Really appreciate it!!).