#!/usr/bin/env python3
# -*- coding: utf-8 -*-
%pylab inline

import folium
import sys
import geopandas as gp
import numpy as np

from coordinate_trans import *
from seoul_gu_list import *
from IPython.display import HTML

def inline_map(map):
    """
    Embeds the HTML source of the map directly into the IPython notebook.

    This method will not work if the map depends on any files (json data). Also this uses
    the HTML5 srcdoc attribute, which may not be supported in all browsers.
    """
    map._build_map()
    return HTML('<iframe srcdoc="{srcdoc}" style="width: 100%; height: 510px; border: none"></iframe>'.format(srcdoc=map.HTML.replace('"', '&quot;')))

def embed_map(map, path="map.html"):
    """
    Embeds a linked iframe to the map into the IPython notebook.

    Note: this method will not capture the source of the map into the notebook.
    This method should work for all maps (as long as they use relative urls).
    """
    map.create_map(path=path)
    return HTML('<iframe src="files/{path}" style="width: 100%; height: 510px; border: none"></iframe>'.format(path=path))

def make_seoul_guname_index_dict():
    l_KOR = list(gdf.SIG_KOR_NM.values)
    l_idx = 0
    seoul_gu_dic = {}
    for seoul_gu in seoul_gu_list:
        for kor_gu in list_KOR:
            if seoul_gu == kor_gu:
                seoul_gu_dic[kor_gu] = list_KOR.index(kor_gu)
    return seoul_gu_dic


# gdf = gp.GeoDataFrame.from_file('seoul_sigun/seoul_sigun.shp', encoding='euc-kr')
gdf = gp.GeoDataFrame.from_file('kor_sigun/kor_shp.shp', encoding='euc-kr')


# seoul = gdf[gdf['Min_min_si'] == '서울특별시'].geometry
# seoul_sigun_polygons = [grs80_to_wgs84(x, y) for x, y in seoul.iloc[0].exterior.coords]


    tileset = 'http://{s}.basemaps.cartocdn.com/light_nolabels/{z}/{x}/{y}.png'

    map_osm = folium.Map(location=[37.5491,126.98955], tiles=tileset, zoom_start=11, attr='cartocdn')

for i in seoul_gu_list:
    geo = gdf[gdf['SIG_KOR_NM'] == i].geometry
    geo_poly = [grs80_to_wgs84(x, y) for x, y in gw.iloc[0].exterior.coords]
    map_osm.line(locations=geo_poly)

embed_map(map_osm)
