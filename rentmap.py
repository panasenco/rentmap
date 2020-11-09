#!/usr/bin/python

import glob
import sys
from typing import Any, Tuple

import folium
import pandas

from geo.utils import aggregate_zip_code_geojsons

STATES_GEO = 'https://raw.githubusercontent.com/python-visualization/folium/master/examples/data/us-states.json'

def midwifery(folium_map: folium.Map = None,
              **kwargs: Any) -> Tuple[str, pandas.DataFrame]:
    midwifery_data = pandas.read_csv(r'.\data\midwifery.csv')
    midwifery_data['total'] = midwifery_data['legality'] + midwifery_data['licensure']
    if folium_map:
        folium.Choropleth(
            name='midwifery',
            geo_data=STATES_GEO,
            data=midwifery_data,
            columns=['state', 'total'],
            key_on='feature.id',
            bins=[0,0.9,1.4,1.6,2],
            fill_color='Purples',
            legend_name='Midwifery Friendliness',
            **kwargs
            ).add_to(folium_map)
    return STATES_GEO, midwifery_data

def gen_zori_geojson():
    # Create a file containing the geojsons of just the ZIP codes in question
    rent_zips_geo, rent_data = zori()
    aggregate_zip_code_geojsons(zips=list(rent_data['RegionName']),
                                outfile=rent_zips_geo)
    

def zori(folium_map: folium.Map = None,
         **kwargs: Any) -> Tuple[str, pandas.DataFrame]:
    rent_zips_geo = './geo/zori_zip_geo.json'
    # Read as string because source data zip codes are sometimes stupidly
    # formatted with leading zeroes
    rent_data = pandas.read_csv(r'C:\Users\apanasenco\Downloads\Zip_ZORI_AllHomesPlusMultifamily_SSA.csv', dtype=str)
    # Convert latest column to int
    value_column = rent_data.columns[-1]
    rent_data[value_column] = rent_data[value_column].astype(float)
    # Drop rent indices over 5,000 (otherwise the legend is all wonky)
    rent_data = rent_data[rent_data[value_column] <= 5000]
    if folium_map:
        folium.Choropleth(
            name='metropolitan rent',
            geo_data=rent_zips_geo,
            data=rent_data,
            columns=['RegionName', value_column],
            key_on='feature.properties.ZCTA5CE10',
            bins=[min(rent_data[value_column]),1000,1200,1400,1600,1800,2000,
                  2200,2400,2600,max(rent_data[value_column])],
            fill_color='Spectral',
            legend_name='Zillow Observed Rent Index (ZORI)',
            **kwargs
            ).add_to(folium_map)
    return rent_zips_geo, rent_data

if __name__ == '__main__':
    m = folium.Map(location=[48, -102], zoom_start=5)
    midwifery(m)
    zori(m, show=False)
    folium.LayerControl().add_to(m)
    m.save('index.html')

