import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pyreadr
    
def gen_map():
    mapdata_d = pyreadr.read_r('../datasets/mapdata_copyright_openstreetmap_contributors.Rds')
    mapdata = np.reshape(to_dec(list(mapdata_d.values())[0].to_numpy()), (-1,1311)).astype(float)

    aspect = mapdata.shape[0] * 1.0 / mapdata.shape[1]
    lon_lat_box = (-88, -87.5, 41.6, 42.1)

    plt.figure(figsize=(10,14))
    plt.imshow(mapdata, 
            cmap=plt.get_cmap('gray'), 
            extent=lon_lat_box, 
            aspect=aspect)

def to_dec(narray):
    for i in range(len(narray)):
        narray[i][0] = int(narray[i][0][1:3],16)/255
    return narray