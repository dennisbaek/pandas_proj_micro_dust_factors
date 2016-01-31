#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pyproj
WGS84 = pyproj.Proj(proj='latlong', datum='WGS84', ellps='WGS84')
TM128 = pyproj.Proj(proj='tmerc', lat_0='38N', lon_0='128E', ellps='bessel', x_0='400000', y_0='600000', k='0.9999', towgs84='-146.43,507.89,681.46')
GRS80 = pyproj.Proj(proj='tmerc', lat_0='38N', lon_0='127.5E', k='0.9996', x_0='1000000', y_0='2000000', ellps='GRS80', units='m')
TM127 = pyproj.Proj(proj='tmerc', lat_0='38N', lon_0='127.0028902777777777776E', ellps='bessel', x_0='200000', y_0='500000', k='1.0', towgs84='-146.43,507.89,681.46')

def wgs84_to_tm128(longitude, latitude):
    lon, lat = pyproj.transform(WGS84, TM128, longitude, latitude )
    return lat, lon

def wgs84_to_tm127(longitude, latitude):
    lon, lat = map(lambda x:2.5*x,
        pyproj.transform(WGS84, TM127, longitude, latitude ))
    return lat, lon

def tm127_to_wgs84(x, y):
    lon, lat = pyproj.transform(TM127, WGS84, x/2.5, y/2.5 )
    return lat, lon

# UTM-K
def grs80_to_wgs84(x, y):
    lon, lat = pyproj.transform(GRS80, WGS84, x, y )
    return lat, lon

# Naver (카텍)
def tm128_to_wgs84(x, y):
    lon, lat = pyproj.transform(TM128, WGS84, x, y)
    return lat, lon
