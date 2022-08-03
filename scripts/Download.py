from urllib.request import urlretrieve
import os


output_relative_dir = '../data/raw/'
target_dir = 'yellow_taxi_data_2019'
YEAR = '2019'
MONTHS = range(1, 13)

if not os.path.exists(output_relative_dir + target_dir):
    os.makedirs(output_relative_dir + target_dir)
            
# data output directory is `data/raw/yellow_taxi_data_2019`
tlc_output_dir = output_relative_dir + 'yellow_taxi_data_2019'

TLC_URL_TEMPLATE = "https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_"#year-month.parquet

for month in MONTHS:
    month = str(month).zfill(2) 
    print(f"Begin month {month}")
    
    # generate url
    url = f'{TLC_URL_TEMPLATE}{YEAR}-{month}.parquet'
    # generate output location and filename
    output_dir = f"{tlc_output_dir}/{YEAR}-{month}.parquet"
    # check if the tlc_data has already been downloaded
    if not os.path.exists(output_dir):
        # download
        urlretrieve(url, output_dir)
    else:
        print("The required tlc_data has already been downloaded")
    
    print(f"Completed month {month}")
    
    
    
external_dir = 'external_data'

if not os.path.exists(output_relative_dir + external_dir):
    os.makedirs(output_relative_dir + external_dir)

external_output_dir = output_relative_dir + 'external_data'
    
    
EXTERNAL_DATA_URL = {
    'nyc_population_by_community_districts.csv': "https://data.cityofnewyork.us/api/views/xi7c-iiu2/rows.csv?accessType=DOWNLOAD"
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

    
    
    


    
    

