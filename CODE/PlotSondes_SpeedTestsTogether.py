#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 13 11:58:34 2025

@author: tylerpelle

Plot a comparison of T/RH from all four speed test (1 m/s, 3 m/s, 5 m/s, and 
8 m/s). 
"""

# Import Python dependencies
import os
import glob
import re
import numpy as np
import pandas as pd
import math
import matplotlib.pyplot as plt

# Load drone data 1 m/s
fpath = '../DATA/DroneData_20250812_132736_1ms.csv'
df1 = pd.read_csv(fpath)
df1['baro_pressure_hpa'] = df1['baro_pressure_pa']/100 
df1_1 = df1[df1['sensorIndex'] == 1]
df1_3 = df1[df1['sensorIndex'] == 3]

# Load drone data 3 m/s
fpath = '../DATA/DroneData_20250812_142820_3ms.csv'
df3 = pd.read_csv(fpath)
df3['baro_pressure_hpa'] = df3['baro_pressure_pa']/100 
df3_1 = df3[df3['sensorIndex'] == 1]
df3_3 = df3[df3['sensorIndex'] == 3]

# Load drone data 5 m/s
fpath = '../DATA/DroneData_20250812_145426_5ms.csv'
df5 = pd.read_csv(fpath)
df5['baro_pressure_hpa'] = df5['baro_pressure_pa']/100 
df5_1 = df5[df5['sensorIndex'] == 1]
df5_3 = df5[df5['sensorIndex'] == 3]

# Load drone data 8 m/s
fpath = '../DATA/DroneData_20250812_150708_8ms.csv'
df8 = pd.read_csv(fpath)
df8['baro_pressure_hpa'] = df8['baro_pressure_pa']/100 
df8_1 = df8[df8['sensorIndex'] == 1]
df8_3 = df8[df8['sensorIndex'] == 3]

# Make temperature compare plot
fig = plt.figure()
plt.style.use('seaborn-v0_8')
plt.plot(df1_3['thermistor_temp_c'],df1_3['baro_pressure_hpa'], label='1 m/s');
plt.plot(df3_3['thermistor_temp_c'],df3_3['baro_pressure_hpa'], label='3 m/s');
plt.plot(df5_3['thermistor_temp_c'],df5_3['baro_pressure_hpa'], label='5 m/s');
plt.plot(df8_3['thermistor_temp_c'],df8_3['baro_pressure_hpa'], label='8 m/s'); 
plt.ylim(df1_3['baro_pressure_hpa'].min(),df1_3['baro_pressure_hpa'].max())
plt.xlim(27,40)
plt.legend()
plt.gca().invert_yaxis()
plt.xlabel('Temperature (DegC)')
plt.ylabel('Pressure (hPa)')
plt.title('Temperature Speed Tests',fontname='Flecha Bronzea M')

# Make RH compare plot
fig = plt.figure()
plt.plot(df1_3['rh_percent'],df1_3['baro_pressure_hpa'], label='1 m/s');
plt.plot(df3_3['rh_percent'],df3_3['baro_pressure_hpa'], label='3 m/s');
plt.plot(df5_3['rh_percent'],df5_3['baro_pressure_hpa'], label='5 m/s');
plt.plot(df8_3['rh_percent'],df8_3['baro_pressure_hpa'], label='8 m/s'); 
plt.ylim(df1_3['baro_pressure_hpa'].min(),df1_3['baro_pressure_hpa'].max())
plt.xlim(20,38)
plt.legend()
plt.gca().invert_yaxis()
plt.xlabel('Relative Humidity (%)')
plt.ylabel('Pressure (hPa)')
plt.title('RH Speed Tests',fontname='Flecha Bronzea M')