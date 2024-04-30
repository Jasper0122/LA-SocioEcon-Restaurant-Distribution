"""
Download the data and store it in the data/raw folder

Author: <Zongrong Li 3707497945 DSCI 510>
"""
from utils.ADI_downloader import download_adi_data
from utils.yelp_downloader import download_yelp_data
from utils.LA_CTs_downloader import download_LA_CTs_data_all_formats

# To download LA_CTs file format. 'csv': 'csv', 'kml': 'kml', 'shp': 'zip', 'geojson': 'geojson'
#download_LA_CTs_data_with_format('csv', 'csv')
download_LA_CTs_data_all_formats()

# To download ADI file format
download_adi_data(save_path='../data/raw')

# To download Yelp file format
download_yelp_data(file_name='raw_yelp_data.csv')

