# %% [code] {"id":"DM4jd7SEHjKf"}
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
from PIL import Image

# %% [code] {"id":"STGzMwAnSnlT"}
#Density
for time_stamp in range(200):#As there are 200 time stamps in total. 
    file = str(time_stamp).zfill(4)#As the file numbers in the data are in the form 0000 to 0199. 
    data_files = pd.read_csv('../input/data-vis/multifield.'+ file + '.zslice.txt', delimiter=' ',header=None)
    
    total_partical_density = data_files[0].values #Selecting first scalar value to visualize to be density
    
    temp = total_partical_density.reshape(248,600) #Keeping z constant and visualizing in X-Y Plane
    fig = plt.figure(figsize=(18,6))
    
    
    plt.contourf(temp, cmap='plasma')
    
    plt.colorbar()
    plt.title("Total Partical density contour map visualization")
    plt.savefig(file+'.jpg') #Directly saving and not doing plt.show()    

#gif generator
grid = []

for time_stamp in range(200):
    file = str(time_stamp).zfill(4)
    img = Image.open(file +'.jpg')
    grid.append(img)

grid[0].save('Total_partical_density.gif',format="GIF",append_images=grid[1:], save_all=True, duration=50, loop=0)

# %% [code] {"id":"1Lhca0aEIe8K","outputId":"0dd0d03e-6d5f-4bd2-bfbc-f6b0ad1fb748"}
#Gas Temperature

for time_stamp in range(200):
    file = str(time_stamp).zfill(4)
    data_files = pd.read_csv('../input/data-vis/multifield.'+ file + '.zslice.txt', delimiter=' ',header=None)
    
    gas_temperature = data_files[1].values
    
    temp = gas_temperature.reshape(248,600)
    fig = plt.figure(figsize=(18,6))
    
    plt.pcolormesh(temp, cmap='inferno')
    plt.colorbar()
    plt.title("Gas Temperature color map visualization")
    
    plt.savefig(file + '.jpg')    

#GIF Generator 
grid = []
    
for time_stamp in range(200):
    file = str(time_stamp).zfill(4)
    img = Image.open(file + '.jpg')
    grid.append(img)

grid[0].save('Gas_Temperature.gif',format="GIF",append_images=grid[1:], save_all=True, duration=50, loop=0)

# %% [code] {"id":"wm9oV9EdQL0l"}
#H mass Abundance

for time_stamp in range(200):
    file = str(time_stamp).zfill(4)
    data_files = pd.read_csv('../input/data-vis/multifield.'+ file + '.zslice.txt', delimiter=' ',header=None)
    
    h_abundance = data_files[2].values
    
    temp = h_abundance.reshape(248,600)
    fig = plt.figure(figsize=(18,6))
    
    plt.pcolormesh(temp, cmap='viridis')
    plt.colorbar()
    plt.title("H Abundance color map visualization")
    
    plt.savefig(file + '.jpg')    

#GIF Generator 
grid = []
    
for time_stamp in range(200):
    file = str(time_stamp).zfill(4)
    img = Image.open(file + '.jpg')
    grid.append(img)

grid[0].save('H_Abundance_color_map.gif',format="GIF",append_images=grid[1:], save_all=True, duration=50, loop=0)

# %% [code]
#H+ mass abundance
for time_stamp in range(200):
    file = str(time_stamp).zfill(4)
    data_files = pd.read_csv('../input/data-vis/multifield.'+ file + '.zslice.txt', delimiter=' ',header=None)
    
    h_plus_abundance = data_files[1].values
    
    temp = h_plus_abundance.reshape(248,600)
    fig = plt.figure(figsize=(18,6))
    
    plt.contourf(temp, cmap='cividis')
    
    plt.colorbar()
    plt.title("H+ mass abundance contour map visualization")
    
    plt.savefig(file + '.jpg')    

#GIF Generator 
grid = []
    
for time_stamp in range(200):
    file = str(time_stamp).zfill(4)
    img = Image.open(file + '.jpg')
    grid.append(img)

grid[0].save('H+_mass_abundance_contour_map.gif',format="GIF",append_images=grid[1:], save_all=True, duration=50, loop=0)
