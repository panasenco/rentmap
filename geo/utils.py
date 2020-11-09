#!/usr/bin/python

import glob
import json
import os
from typing import List

GEO_DIR = os.path.dirname(os.path.abspath(__file__))

def aggregate_zip_code_geojsons(zips: List[str] = None, outfile: str = None):
    agg = {'type': 'FeatureCollection', 'features': []}
    for geofile in glob.iglob(f'{GEO_DIR}/State-zip-code-GeoJSON/*_zip_codes_geo.min.json'):
        print(f'Aggregating from {geofile}')
        with open(geofile) as f:
            state_zips = json.load(f)
            agg['features'] += [feature for feature in state_zips['features'] if zips is None or feature['properties']['ZCTA5CE10'] in zips]
    if outfile is not None:
        with open(outfile, 'w') as f:
            json.dump(agg, f, separators=(',',':'))
    return agg
