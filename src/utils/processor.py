# utils/processor.py Author: <Zongrong Li 3707497945 DSCI 510>

import pandas as pd
import zipfile
import os

def process_adi_data(input_path, output_path):
    # Define the path for the extracted files
    extract_path = os.path.join(os.path.dirname(input_path), 'extracted')

    # Create a directory for extracted files if it doesn't exist
    if not os.path.exists(extract_path):
        os.makedirs(extract_path)

    # Extract the zip file
    with zipfile.ZipFile(input_path, 'r') as zip_ref:
        zip_ref.extractall(extract_path)

    # Find all CSV files in the extracted directory
    csv_files = [file for file in os.listdir(extract_path) if file.endswith('.csv')]

    # Initialize a list to collect dataframes
    dataframes = []

    # Process each CSV file
    for csv_file in csv_files:
        # Construct full file path
        file_path = os.path.join(extract_path, csv_file)

        # Read the CSV file
        df = pd.read_csv(file_path)

        # Check if 'FIPS' and 'ADI_NATRANK' columns are in the dataframe
        if 'FIPS' in df.columns and 'ADI_NATRANK' in df.columns:
            # Select only 'FIPS' and 'ADI_NATRANK'
            df_processed = df[['FIPS', 'ADI_NATRANK']].copy()

            # Convert non-numeric ADI_NATRANK values to NaN and drop rows with NaN
            df_processed['ADI_NATRANK'] = pd.to_numeric(df_processed['ADI_NATRANK'], errors='coerce')
            df_processed.dropna(subset=['ADI_NATRANK'], inplace=True)

            # Bin 'ADI_NATRANK' into 3 categories
            # For example, let's say we decide the bins as follows:
            # 0 - 33 percentile, 34 - 66 percentile, 67 - 100 percentile
            # The exact bins will depend on the distribution of your data.
            df_processed['ADI_NATRANK_Category'] = pd.qcut(df_processed['ADI_NATRANK'], q=3, labels=[0, 1, 2])

            # Add to the list of dataframes
            dataframes.append(df_processed)
        else:
            print(f'The file {csv_file} does not contain the required columns.')

    # Concatenate all dataframes
    all_data = pd.concat(dataframes, ignore_index=True)

    # Remove any duplicates that might have come from multiple CSVs
    all_data.drop_duplicates(inplace=True)

    # Write the combined and processed dataframe to a new CSV file in the processed directory
    output_file_path = os.path.join(output_path, 'adi_data.csv')
    all_data.to_csv(output_file_path, index=False)

    print(f"Cleaning complete. Saved in '{output_path}/adi_data.csv'")
    return output_file_path


def process_LA_CTs_zip(raw_zip_path, processed_directory):

    # Construct the path for the extracted folder
    extracted_folder_name = "LA_CTs"
    extracted_folder_path = os.path.join(processed_directory, extracted_folder_name)

    # Create the 'processed' directory if it doesn't exist
    if not os.path.exists(processed_directory):
        os.makedirs(processed_directory)

    # Extract the ZIP file into the 'processed' directory
    with zipfile.ZipFile(raw_zip_path, 'r') as zip_ref:
        zip_ref.extractall(extracted_folder_path)

    print(f"Extraction complete. Folder '{extracted_folder_name}' extracted to: {processed_directory}")

def process_raw_yelp_data(input_path, output_path):
    # Load the raw Yelp data with the correct encoding
    raw_data = pd.read_csv(input_path, encoding='ISO-8859-1')

    # Remove 'name' column (equivalent to 'NAME')
    raw_data.drop('name', axis=1, inplace=True)

    # Bin 'review_count' into 3 categories (assuming 'review_count' is equivalent to 'Review_num')
    review_bins = [0, 100, 500, float('inf')]
    review_labels = [0, 1, 2]
    raw_data['Review_num'] = pd.cut(raw_data['review_count'], bins=review_bins, labels=review_labels)

    # Bin 'rating' into 3 categories
    rating_bins = [0, 2, 4, 5]
    rating_labels = [0, 1, 2]
    raw_data['Rating'] = pd.cut(raw_data['rating'], bins=rating_bins, labels=rating_labels)

    # Bin 'price' into 3 categories (0 for $, 1 for $$, and 2 for $$$ and above)
    price_map = {'$': 0, '$$': 1, '$$$': 2, '$$$$': 2}
    raw_data['Price'] = raw_data['price'].map(price_map)

    # Process 'categories' to extract the 'title' values
    raw_data['Categories'] = raw_data['categories'].apply(lambda x: ', '.join([d['title'] for d in eval(x)]))

    # Extract latitude and longitude from 'coordinates'
    raw_data['latitude'] = raw_data['coordinates'].apply(lambda x: eval(x)['latitude'])
    raw_data['longitude'] = raw_data['coordinates'].apply(lambda x: eval(x)['longitude'])

    # Ensure only to select columns that exist in the raw_data to avoid KeyError
    final_columns = ['id', 'latitude', 'longitude', 'Review_num', 'Rating', 'Categories', 'Price']
    existing_columns = [col for col in final_columns if col in raw_data.columns]
    processed_data = raw_data[existing_columns]

    # Save the processed data to the specified output path with UTF-8 encoding
    processed_data.to_csv(output_path, index=False, encoding='utf-8')
    print(f"Cleaning complete. Saved in '{output_path}'")

