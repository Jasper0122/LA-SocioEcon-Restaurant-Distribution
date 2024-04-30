# utils/LA_CTs_downloader.py Author: <Zongrong Li 3707497945 DSCI 510>

import requests
import os

# define the headers and format_dict at the module level
headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'Connection': 'keep-alive',
    'Referer': 'https://geohub.lacity.org/',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'cross-site',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 Edg/123.0.0.0',
    'sec-ch-ua': '"Microsoft Edge";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

format_dict = {'csv': 'csv', 'kml': 'kml', 'shp': 'zip', 'geojson': 'geojson'}

def download_LA_CTs_data_with_format(request_format, file_format, save_path='../data/raw'):
    params = (
        ('format', request_format),
        ('spatialRefId', '4326'),
        ('where', '1=1'),
    )
    response = requests.get('https://opendata.arcgis.com/api/v3/datasets/a3c75dfcba8f469c882a726ba99d1cfa_0/downloads/data', headers=headers, params=params)

    # if success
    if response.status_code == 200:
        file_name = f'LA_City_2020_Census_Tracts_.{file_format}'
        full_path = os.path.join(save_path, file_name)
        # Ensure the directory exists
        os.makedirs(save_path, exist_ok=True)
        # writing response to file
        with open(full_path, 'wb') as file:
            file.write(response.content)
        print(f"Successfully saved File as {full_path}")
    else:
        print("Response Error, Status Code:", response.status_code)

# function to download all formats
def download_LA_CTs_data_all_formats():
    for request_format, file_format in format_dict.items():
        download_LA_CTs_data_with_format(request_format, file_format)
