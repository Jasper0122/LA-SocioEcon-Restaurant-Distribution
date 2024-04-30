"""
Clean the data, transform the data and store the files in the data/processed folder

Author: <Zongrong Li 3707497945 DSCI 510>
"""

from utils.processor import process_raw_yelp_data, process_adi_data, process_LA_CTs_zip

# Process raw yelp Data
process_raw_yelp_data('../data/raw/raw_yelp_data.csv','../data/processed/yelp_data.csv')

# Process raw ADI Data
process_adi_data('../data/raw/adi-download.zip','../data/processed')

# Process LA_CTs Data
process_LA_CTs_zip('../data/raw/LA_City_2020_Census_Tracts_.zip', '../data/processed')