# utils/yelp_downloader.py Author: <Zongrong Li 3707497945 DSCI 510>
import requests
import csv
import os
import time

# Constants
API_KEY = 'NFPWCChl94oCIGYBJJWC_HBRNLxCVzrVxl_U0UZSAKJC3ghcrNlcxuGkG5RkPSlfXaZOS09psuwDqCSHKLL5UE7_OJCqb7iOnmX8LhZgZuO0AknoxNVwxq9jlWIYZnYx'
ENDPOINT = 'https://api.yelp.com/v3/businesses/search'
HEADERS = {'Authorization': f'bearer {API_KEY}'}


def scrape_data(scrape_limit=None, location='Los Angeles'):
    parameters = {
            'term': 'restaurants',
            'limit': 50 if not scrape_limit else scrape_limit,
            'location': location,
            'offset': 0
    }

    businesses = []
    start_time = time.time()

    while True:
        if time.time() - start_time > 3:  # Check if 5 seconds have passed
            print("Yelp Data Downloading...")
            start_time = time.time()

        response = requests.get(url=ENDPOINT, params=parameters, headers=HEADERS)
        if response.status_code != 200:
            # print(f"Response Error, Status Code: {response.status_code}")
            break

        data = response.json()
        businesses.extend(data.get('businesses', []))

        if scrape_limit and len(businesses) >= scrape_limit:
            businesses = businesses[:scrape_limit]
            break

        if len(data.get('businesses', [])) < parameters['limit']:
            break

        parameters['offset'] += parameters['limit']

    return businesses


def save_to_csv(businesses, file_path):
    if businesses:
        # Collect all unique keys from all dictionaries
        fieldnames = list({key for business in businesses for key in business.keys()})

        with open(file_path, mode='w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for business in businesses:
                # If a business does not have all the fields, the missing ones will be empty in the CSV
                writer.writerow(business)
        print(f"Successfully saved file as {file_path}")


def download_yelp_data(scrape_limit=None, location='Los Angeles', file_name='yelp_data.csv'):
    businesses = scrape_data(scrape_limit, location)
    # Make sure the directory exists
    raw_dir_path = '../data/raw'  # Assuming this is run from within the src directory
    os.makedirs(raw_dir_path, exist_ok=True)

    # Create the full file path
    file_path = os.path.join(raw_dir_path, file_name)

    # Save the businesses data to CSV file
    save_to_csv(businesses, file_path)

