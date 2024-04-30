# utils/Geospatial_join.py Author: <Zongrong Li 3707497945 DSCI 510>

import geopandas as gpd
import pandas as pd

def perform_spatial_join(yelp_data_path, tracts_shp_path):
    # Load Yelp data
    yelp_data = pd.read_csv(yelp_data_path)

    # Convert DataFrame to GeoDataFrame
    gdf_yelp = gpd.GeoDataFrame(yelp_data, geometry=gpd.points_from_xy(yelp_data.longitude, yelp_data.latitude))

    # Set the coordinate reference system (CRS) for Yelp data to WGS84
    gdf_yelp.set_crs(epsg=4326, inplace=True)

    # Load census tracts shapefile
    gdf_tracts = gpd.read_file(tracts_shp_path)

    # Ensure both GeoDataFrames use the same CRS
    gdf_tracts = gdf_tracts.to_crs(gdf_yelp.crs)

    # Perform the spatial join using the new 'predicate' parameter
    gdf_joined = gpd.sjoin(gdf_yelp, gdf_tracts, how='left', predicate='intersects')

    # Modify CT20 values by adding the prefix '60037'
    gdf_joined['CT20'] = gdf_joined['CT20'].apply(lambda x: f'6037{x}' if pd.notnull(x) else x)

    # Convert GeoDataFrame to DataFrame and drop the geometry column
    df_joined = pd.DataFrame(gdf_joined.drop(columns='geometry'))

    print("Spatial join completed")
    return df_joined
