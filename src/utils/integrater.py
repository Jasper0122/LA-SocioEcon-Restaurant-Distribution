# utils/integrator.py Author: <Zongrong Li 3707497945 DSCI 510>
import pandas as pd

def merge_and_fuzzy_match(adi_data_path, yelp_data):
    # Load the ADI data
    adi_data = pd.read_csv(adi_data_path)

    # Preprocess ADI data: remove the last digit and convert to string for fuzzy matching
    adi_data['FIPS_modified'] = adi_data['FIPS'].astype(str).str[:-1]
    adi_data['FIPS_modified_str'] = adi_data['FIPS_modified'].str[:8]  # Using only the first 8 digits

    # Preprocess Yelp data: convert CT20 to string for fuzzy matching
    yelp_data['CT20_str'] = yelp_data['CT20'].astype(str)
    yelp_data['CT20_fuzzy'] = yelp_data['CT20_str'].str[:8]  # Using only the first 8 digits

    # Perform the fuzzy merge
    merged_data = pd.merge(yelp_data, adi_data, left_on='CT20_fuzzy', right_on='FIPS_modified_str', how='left')

    return merged_data


def filter_and_save_csv(data, output_path):
    # Load the dataset

    columns = [
        'latitude',
        'longitude',
        'Review_num',
        'Rating',
        'Categories',
        'Price',
        'ADI_NATRANK',
        'ADI_NATRANK_Category'
    ]

    # Filter the dataset to only include the specified columns
    filtered_data = data[columns]

    # Save the filtered data to a new CSV file
    filtered_data.to_csv(output_path, index=False)
    print(f"Integrated data saved to {output_path}")