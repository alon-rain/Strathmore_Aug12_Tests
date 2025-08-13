#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 13 11:41:48 2025

@author: tylerpelle

Process sonde and drone flights for the speed tests. Here, we are individually
plotting each speed test against the sonde that was closest in time (sonde-2 in
the DATA directory). Note that sonde-1 should have been the comparison here, but
the computer over-heated and caused us to lose data. We needed to cool the computer
down and then launch sonde-2, which took place ~20 minutes after the conclusion
of these flights. So I don't think the sondes are very representative because
it definitely got hotter between the time the flights started and when we 
launched sonde-2

NOTE: Below, change the variable "speed" to either 1, 3, 5, or 8 to plot that 
respective speed test
"""

# Import Python dependencies
import os
import glob
import re
import numpy as np
import pandas as pd
import math
import matplotlib.pyplot as plt

# Set drone-speed to plot
speed = 1

##############
# Sonde Data
##############
# Load in data file and construct dataframe
fpath = '../DATA/Sonde2_20250812230024064606.txt'
df = pd.read_csv(fpath, delim_whitespace=True, header=3, encoding='latin-1') 
df.columns = ['Time (sec)','Time (UTC)','P (hPa)','T (DegC)','Hu (%)','Ws (m/s)','Wd (Deg)','Geopot (m)','Dewp (DegC)']

# Trim off end rows
df = df[:-6]

# Convert allcolumns except Time (UTC) to float
exclude_col = 'Time (UTC)'
cols_to_convert = [col for col in df.columns if col != exclude_col]
df[cols_to_convert] = df[cols_to_convert].astype(float)

##############
# Drone Data 
##############
if speed==1:
    fpath = '../DATA/DroneData_20250812_132736_1ms.csv'
elif speed==3:
    fpath = '../DATA/DroneData_20250812_142820_3ms.csv'
elif speed==5:
    fpath = '../DATA/DroneData_20250812_145426_5ms.csv'
elif speed==8:
    fpath = '../DATA/DroneData_20250812_150708_8ms.csv'       
dfd = pd.read_csv(fpath)
dfd['baro_pressure_hpa'] = dfd['baro_pressure_pa']/100 
dfd_1 = dfd[dfd['sensorIndex'] == 1]
dfd_3 = dfd[dfd['sensorIndex'] == 3]

##############
# Make Plot
##############
# Temperature
fig = plt.figure()
plt.style.use('rm_technical')
plt.plot(dfd_1['thermistor_temp_c'],dfd_1['baro_pressure_hpa'], label='Drone S1'); 
plt.plot(dfd_3['thermistor_temp_c'],dfd_3['baro_pressure_hpa'], label='Drone S3'); 
plt.plot(df['T (DegC)'],df['P (hPa)'], label='Sonde')
plt.ylim(dfd_1['baro_pressure_hpa'].min(),dfd_1['baro_pressure_hpa'].max())
plt.xlim(27,40)
plt.legend()
plt.gca().invert_yaxis()
plt.xlabel('Temperature (DegC)')
plt.ylabel('Pressure (hPa)')
plt.title(f'Temperature: Drone Speed {speed} m/s',fontname='Flecha Bronzea M')

# Humidity
fig = plt.figure()
plt.plot(dfd_1['rh_percent'],dfd_1['baro_pressure_hpa'], label='Drone S1');
plt.plot(dfd_3['rh_percent'],dfd_3['baro_pressure_hpa'], label='Drone S3');  
plt.plot(df['Hu (%)'],df['P (hPa)'], label='Sonde')
plt.ylim(dfd_1['baro_pressure_hpa'].min(),dfd_1['baro_pressure_hpa'].max())
plt.xlim(20,38)
plt.legend()
plt.gca().invert_yaxis()
plt.xlabel('Relative Humidity (%)')
plt.ylabel('Pressure (hPa)')
plt.title(f'RH: Drone Speed {speed} m/s',fontname='Flecha Bronzea M')
