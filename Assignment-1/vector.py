# %% [code] {"execution":{"iopub.status.busy":"2021-09-02T14:57:32.483709Z","iopub.execute_input":"2021-09-02T14:57:32.484086Z","iopub.status.idle":"2021-09-02T14:57:32.489448Z","shell.execute_reply.started":"2021-09-02T14:57:32.484056Z","shell.execute_reply":"2021-09-02T14:57:32.488408Z"},"jupyter":{"outputs_hidden":false}}
import os
import pandas as pd
import numpy as np
from tqdm import tqdm
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from matplotlib.colors import Normalize

# %% [code] {"execution":{"iopub.status.busy":"2021-09-02T15:21:06.064932Z","iopub.execute_input":"2021-09-02T15:21:06.065304Z","iopub.status.idle":"2021-09-02T18:40:19.201844Z","shell.execute_reply.started":"2021-09-02T15:21:06.065275Z","shell.execute_reply":"2021-09-02T18:40:19.200505Z"},"jupyter":{"outputs_hidden":false}}
#index_time_stamp=119
for i in range(200):

    time_stamp = str(i).zfill(4)
    
    file = '../input/dv-data-1/velocity.' + time_stamp + '.txt'
    
    if not os.path.isfile(file):
        continue
    
    #reading data
    data_file = pd.read_csv(file,delimiter=' ',header=None)
    data_file = np.array(data_file)
    
    #Initialize and define velocity vector
    velocity = np.zeros((600,248,248,3))
    
    temp1 = 0
    for k in range(248):
        for j in range (248):
            for x in range(600):
                velocity[x][j][k][2] = data_file[temp1][2]
                velocity[x][j][k][1] = data_file[temp1][1]
                velocity[x][j][k][0] = data_file[temp1][0]
                temp1 = temp1 +1
    
    #Utilizing velocity curl AS MOENTIONED ON WEBSITE
    velocity_curl = np.zeros((36902400, 3)) # 248*248*600 = 36902400
    
    temp2 = -1
    
    for k in range(248):
        for j in range(248):
            for x in range(600):
                temp2 = temp2 + 1
                if  x == 599 or j == 247 or k == 247 :
                    continue
                else:                    
                    velocity_curl[temp2][0] = ( velocity[x][j+1][k][2] - velocity[x][j][k][2] - velocity[x][j][k+1][1] + velocity[x][j][k][1] ) / 0.001
                    velocity_curl[temp2][1] = ( velocity[x][j][k+1][0] - velocity[x][j][k][0] - velocity[x+1][j][k][2] + velocity[x][j][k][2] ) / 0.001
                    velocity_curl[temp2][2] = ( velocity[x+1][j][k][1] - velocity[x][j][k][1] - velocity[x][j+1][k][0] + velocity[x][j][k][0] ) / 0.001
    
    #Using the below value as data available for it            
    z=124
    velocity_curl = velocity_curl [z*600*248 : (z+1)*600*248]

    curl_i = np.array(velocity_curl[:,0]).reshape(248,600)
    curl_j = np.array(velocity_curl[:,1]).reshape(248,600)
    curl_k = np.array(velocity_curl[:,2]).reshape(248,600)
    
    #plotting figure

    file = time_stamp + '.jpg'
    
    fig = plt.figure(figsize=(30,10))
    
    plt.quiver(np.arange(600), np.arange(248), curl_i, curl_j, scale=10000.0 , scale_units='width', width=1e-3)
    plt.title("Velocity vector quiver plot visualization")

    plt.savefig(file)
    plt.show()

# %% [code] {"execution":{"iopub.status.busy":"2021-09-02T18:46:41.598830Z","iopub.execute_input":"2021-09-02T18:46:41.599222Z","iopub.status.idle":"2021-09-02T18:46:42.437484Z","shell.execute_reply.started":"2021-09-02T18:46:41.599191Z","shell.execute_reply":"2021-09-02T18:46:42.436189Z"},"jupyter":{"outputs_hidden":false}}
from PIL import Image
grid = []

for i in range(200):

    time_stamp = str(i).zfill(4)
    file = time_stamp + '.jpg'
    if not os.path.isfile(file):
        continue
    
    img = Image.open(file)
    grid.append(img)
    
grid[0].save('vector.gif',format="GIF",append_images=grid[1:], save_all=True, duration=150, loop=0)
