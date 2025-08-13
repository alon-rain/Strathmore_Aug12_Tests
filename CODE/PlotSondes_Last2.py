#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 13 09:56:43 2025

@author: tylerpelle

Process sondes and drone flights for the last two radiation-shield flight tests
"""

# Import Python dependencies
import os
import glob
import re
import numpy as np
import pandas as pd
import math
import matplotlib.pyplot as plt

##############
# Sonde Data
##############
# Load in data file and construct dataframe
fpath = '../DATA/Sonde3_20250812220024064561.txt'
df = pd.read_csv(fpath, sep='\s+', header=3, encoding='latin-1') 
df.columns = ['Time (sec)','Time (UTC)','P (hPa)','T (DegC)','Hu (%)','Ws (m/s)','Wd (Deg)','Geopot (m)','Dewp (DegC)']

# Trim off end rows
df = df[:-6]

# Convert allcolumns except Time (UTC) to float
exclude_col = 'Time (UTC)'
cols_to_convert = [col for col in df.columns if col != exclude_col]
df[cols_to_convert] = df[cols_to_convert].astype(float)

# Get rid of error in RH
df = df[(df['Hu (%)'] >= 20)]

##############
# Drone Data
##############
fpath = '../DATA/DroneData_20250812_152456.csv'
df2 = pd.read_csv(fpath)
df2['baro_pressure_hpa'] = df2['baro_pressure_pa']/100 
df2_1 = df2[df2['sensorIndex'] == 1]
df2_3 = df2[df2['sensorIndex'] == 3]

# Split up the two flights
df2_11 = df2_1[0:2000]
df2_12 = df2_1[2001:4000]
df2_31 = df2_3[0:2000]
df2_32 = df2_3[2001:4000]

##############
# Comparative plots - flight 1
##############
# Temperature
fig = plt.figure()
plt.style.use('seaborn-v0_8')
plt.plot(df2_11['thermistor_temp_c'],df2_11['baro_pressure_hpa'], label='Drone S1'); 
plt.plot(df2_31['thermistor_temp_c'],df2_31['baro_pressure_hpa'], label='Drone S3'); 
plt.plot(df['T (DegC)'],df['P (hPa)'], label='Sonde')
plt.ylim(df2_11['baro_pressure_hpa'].min(),df2_11['baro_pressure_hpa'].max())
plt.xlim(27,40)
plt.legend()
plt.gca().invert_yaxis()
plt.xlabel('Temperature (DegC)')
plt.ylabel('Pressure (hPa)')
plt.title('Temperature: Flight-1',fontname='Flecha Bronzea M')

# Humidity
fig = plt.figure()
plt.plot(df2_11['rh_percent'],df2_11['baro_pressure_hpa'], label='Drone S1');
plt.plot(df2_31['rh_percent'],df2_31['baro_pressure_hpa'], label='Drone S3');  
plt.plot(df['Hu (%)'],df['P (hPa)'], label='Sonde')
plt.ylim(df2_11['baro_pressure_hpa'].min(),df2_11['baro_pressure_hpa'].max())
plt.xlim(20,33)
plt.legend()
plt.gca().invert_yaxis()
plt.xlabel('Relative Humidity (%)')
plt.ylabel('Pressure (hPa)')
plt.title('RH: Flight-1',fontname='Flecha Bronzea M')

##############
# Comparative plots - flight 2
##############
# Temperature
fig = plt.figure()
plt.style.use('seaborn-v0_8')
plt.plot(df2_12['thermistor_temp_c'],df2_12['baro_pressure_hpa'], label='Drone S1'); 
plt.plot(df2_32['thermistor_temp_c'],df2_32['baro_pressure_hpa'], label='Drone S3'); 
plt.plot(df['T (DegC)'],df['P (hPa)'], label='Sonde')
plt.ylim(df2_12['baro_pressure_hpa'].min(),df2_12['baro_pressure_hpa'].max())
plt.xlim(27,40)
plt.legend()
plt.gca().invert_yaxis()
plt.xlabel('Temperature (DegC)')
plt.ylabel('Pressure (hPa)')
plt.title('Temperature: Flight-2',fontname='Flecha Bronzea M')

# Humidity
fig = plt.figure()
plt.plot(df2_12['rh_percent'],df2_12['baro_pressure_hpa'], label='Drone S1');
plt.plot(df2_32['rh_percent'],df2_32['baro_pressure_hpa'], label='Drone S3');  
plt.plot(df['Hu (%)'],df['P (hPa)'], label='Sonde')
plt.ylim(df2_12['baro_pressure_hpa'].min(),df2_12['baro_pressure_hpa'].max())
plt.xlim(20,33)
plt.legend()
plt.gca().invert_yaxis()
plt.xlabel('Relative Humidity (%)')
plt.ylabel('Pressure (hPa)')
plt.title('RH: Flight-2',fontname='Flecha Bronzea M')

# Plotting all three temperatures for flights
fig = plt.figure()
plt.style.use('seaborn-v0_8')
plt.plot(df2_32['sht_temp_c'],df2_32['baro_pressure_hpa'], label='S3-sht')
plt.plot(df2_32['baro_temp_c'],df2_32['baro_pressure_hpa'], label='S3-baro')
plt.plot(df2_32['thermistor_temp_c'],df2_32['baro_pressure_hpa'], label='S3-thermistor')
plt.xlim(27,40)
plt.legend()
plt.gca().invert_yaxis()
plt.xlabel('Temperature (DegC)')
plt.ylabel('Pressure (hPa)')
plt.title('Flight-2, Sensor-3- Temperature Comparison',fontname='Flecha Bronzea M')


