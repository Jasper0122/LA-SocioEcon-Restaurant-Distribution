
# Geospatial Analysis of Socioeconomic Status and Restaurant Distribution in LA

## Short Description

This data science project aims to perform a geospatial analysis of socioeconomic status and its impact on restaurant distribution across Los Angeles County. By leveraging diverse web sources, this study examines the correlation between socioeconomic factors — like education and income — and the variety of restaurants available in different areas. The goal is to understand how these elements influence food service diversity, contributing valuable insights into urban planning and social equity.

### Author

Zongrong Li

Email: zongrong[at]usc[dot]edu

Personal website: [Zongrong (Jasper)](https://jasper0122.github.io/)

## Purpose

The project explores the intricate relationship between community socioeconomic conditions and the resultant distribution of food services. It aims to uncover patterns that reveal the influence of educational, income, and other socioeconomic factors on restaurant diversity, providing a data-driven approach to understanding economic development and social dynamics within LA County.

## Data Source and Collection Method

Data is extracted from multiple sources using a variety of data science techniques:

- **Yelp API**: To gather detailed restaurant information.
  - Documentation: [Yelp Fusion API](https://docs.developer.yelp.com/docs/fusion-intro)

- **LA Geo Hub API**: For geospatial data and demographic insights.
  - Documentation: [LA Geo Hub API](https://geohub.lacity.org/datasets/a3c75dfcba8f469c882a726ba99d1cfa_0/explore?location=34.065170%2C-118.125855%2C10.74)

- **Area Deprivation Index (ADI)**: For socioeconomic indicators.
  - Documentation: [Neighborhood Atlas](https://www.neighborhoodatlas.medicine.wisc.edu/)

These sources are processed through automated scripts utilizing Python's BeautifulSoup for web scraping, the `requests` library for API interaction, and `pandas` for structuring and cleaning the data.

## Installation and Usage

Install the required dependencies as follows:

```bash
pip install -r requirements.txt
```

### Running the Data Collection Scripts

Navigate to the `src` directory and execute the following scripts:

```bash
python get_data.py        # For data extraction from the APIs and web sources
python clean_data.py      # For data cleaning and preprocessing
python integrate_data.py  # For data integration and preparation for analysis
```

### Analyzing and Visualizing the Data

Run the analysis and visualization notebook with:

```bash
python analyze_visualize.py 
jupyter notebook analyze_visualize.ipynb #in the `results` directory
```

## Deliverables

- `proposal.pdf`: A comprehensive proposal of the project located in the root directory.
- `final_report.pdf`: The detailed final report with analyses and conclusions in the `results` directory.
- `src/`: Contains all the source code and Jupyter notebooks for the project.

## Project Outcomes

The insights derived from this study will provide stakeholders with an understanding of how socioeconomic factors shape the cultural landscape of LA County. The visualizations created will illustrate the socio-demographic diversity and its relationship with the local restaurant industry.

## Further Information

For more detailed information on how to use the APIs and extract data, please refer to the links provided in the Data Source section.

## License

This project is released under the MIT License. See LICENSE.md for more details.
