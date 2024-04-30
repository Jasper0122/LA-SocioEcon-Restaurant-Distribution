"""
Integrates all the data into a format that can be easily analyzed
This will probably take the form of merging (joining) several Pandas
DataFrames, or issuing SQL queries over tables in a relational DB.

Author: <Zongrong Li 3707497945 DSCI 510>
"""
from utils.Geospatial_join import perform_spatial_join
from utils.integrater import merge_and_fuzzy_match, filter_and_save_csv


# Geospatial join the yelp and LA_CTs datas
yelp_data_path = '../data/processed/yelp_data.csv'
tracts_shp_path = '../data/processed/LA_CTs/LA_City_2020_Census_Tracts_.shp'
joined_df = perform_spatial_join(yelp_data_path, tracts_shp_path)


# Integrate datas
adi_data_path = '../data/processed/adi_data.csv'
yelp_data = joined_df
merged_data = merge_and_fuzzy_match(adi_data_path, yelp_data)



# Cleans the merged data
output_path = '../data/processed/integrated_data.csv'
filter_and_save_csv(merged_data, output_path)
