#!/usr/bin/python

import glob
import sys

import folium
import pandas

def get_geo_data(state: str):
    return next(glob.iglob(f'.\State-zip-code-GeoJSON\{state.lower()}_*_zip_codes_geo.min.json'))

def get_rent_data(state: str):
    rent_data = pandas.read_csv(r'C:\Users\apanasenco\Downloads\Zip_ZORI_AllHomesPlusMultifamily_SSA.csv')
    rent_data['RegionName'] = rent_data['RegionName'].astype(str)
    return rent_data[rent_data['MsaName'].str.contains(f', {state.upper()}')]

if __name__ == '__main__':
    state = sys.argv[1]
    print(f'State: {state}')
    m = folium.Map(location=[48, -102], zoom_start=5)
    folium.Choropleth(
        geo_data=get_geo_data(state),
        data=get_rent_data(state),
        columns=['RegionName', '2020-08'],
        key_on='feature.properties.ZCTA5CE10',
        legend_name='Zillow Rent Index'
        ).add_to(m)
    m.save('index.html')

