from urllib.request import urlretrieve
import os
from zipfile import ZipFile

# Download tlc data from 2019 and 2020
output_relative_dir = '../data/raw/'
target_dir = 'yellow_taxi_data_'
YEARS = ['2019', '2020']
MONTHS = range(1, 13)

for year in YEARS:
    if not os.path.exists(output_relative_dir + target_dir + year):
        os.makedirs(output_relative_dir + target_dir + year)


TLC_URL_TEMPLATE = "https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_"#year-month.parquet

for year in YEARS:
    print(f"Begin year {year}")
    for month in MONTHS:
        month = str(month).zfill(2) 
        print(f"Begin month {month}")
    
        # generate url
        url = f'{TLC_URL_TEMPLATE}{year}-{month}.parquet'
        # generate output location and filename
        output_dir = f"{output_relative_dir + target_dir + year}/{year}-{month}.parquet"
        # check if the tlc_data has already been downloaded
        if not os.path.exists(output_dir):
            # download
            urlretrieve(url, output_dir)
        else:
            print("The required tlc_data has already been downloaded")
    
        print(f"Completed month {month}")
    print(f"Completed year {year}")
    
    
    
# Download externel data and taxi zones data
external_dir = 'external_data_and_taxi_zones'

if not os.path.exists(output_relative_dir + external_dir):
    os.makedirs(output_relative_dir + external_dir)

external_output_dir = output_relative_dir + 'external_data_and_taxi_zones'
    
    
EXTERNAL_DATA_URL = {
    'nyc_population_by_community_districts.csv': "https://data.cityofnewyork.us/api/views/xi7c-iiu2/rows.csv?accessType=DOWNLOAD",
    'taxi_zone_lookup.csv': "https://s3.amazonaws.com/nyc-tlc/misc/taxi+_zone_lookup.csv",
    'taxi_zones.zip': "https://d37ci6vzurychx.cloudfront.net/misc/taxi_zones.zip"
    }


for dataset_name, url in EXTERNAL_DATA_URL.items():
    print(f"Begin {dataset_name}")
    
    # generate output location and filename
    output_dir = f"{external_output_dir}/{dataset_name}"
    # check if the data has already been downloaded
    if not os.path.exists(output_dir):
        # download
        urlretrieve(url, output_dir)
    else:
        print(f"The required {dataset_name} has already been downloaded")
    
    print(f"Completed {dataset_name}")
    


# Unzip taxi_zone data
output_dir = output_relative_dir + 'external_data_and_taxi_zones' + "/taxi_zones"

if not os.path.exists(output_dir):
    os.makedirs(output_dir)
    
taxi_zones_fp = "../data/raw/external_data_and_taxi_zones/taxi_zones.zip"

with ZipFile(taxi_zones_fp, 'r') as zip_ref:
    zip_ref.extractall(output_dir)
    print(f'Completed extraction {taxi_zones_fp}')

    
# Remove the zipfile
os.remove(external_output_dir + '/taxi_zones.zip')



    
  

    
    


    
    

