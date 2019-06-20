# In[1]:
import geopandas as gpd
import matplotlib.pyplot as plt
import os
import numpy as np
import earthpy as et

# plot data inline
plt.ion() 

%matplotlib inline
plt.rcParams['figure.figsize'] = (30, 30)

#os.chdir(os.path.join(et.io.HOME, 'E:\Dataset Telco'))



# In[2]:
geo_milano = 'E:\Dataset Telco\Examples\milano-grid.geojson'
shp_LIM010102 = 'E:\Dataset Telco\DBT2012_STRATO01_E0\LIM_010102.shp'
shp_LIM010103 = 'E:\Dataset Telco\DBT2012_STRATO01_E0\LIM_010103.shp'
shp_LIM010104 = 'E:\Dataset Telco\DBT2012_STRATO01_E0\LIM_010104.shp'
shp_LIM010105 = 'E:\Dataset Telco\DBT2012_STRATO01_E0\LIM_010105.shp'

map_LIM010102 = gpd.read_file(shp_LIM010102)
map_LIM010103 = gpd.read_file(shp_LIM010103)
map_LIM010104 = gpd.read_file(shp_LIM010104)
map_LIM010105 = gpd.read_file(shp_LIM010105)
milano = gpd.read_file(geo_milano)



# In[3]
map_LIM010102_wgs84 = map_LIM010102.to_crs({'init': 'epsg:4326'})
map_LIM010103_wgs84 = map_LIM010103.to_crs({'init': 'epsg:4326'})
map_LIM010104_wgs84 = map_LIM010104.to_crs({'init': 'epsg:4326'})
map_LIM010105_wgs84 = map_LIM010105.to_crs({'init': 'epsg:4326'})



# In[4]:
fig, ax = plt.subplots(figsize = (20,20))
ax.set_title('Movilidad y Transporte\nMilano')
ax.set_axis_off()
plt.axis('equal');

map_LIM010102_wgs84.plot(color='green',
                         edgecolor = 'black',
                         ax = ax,
                         legend = 'Peatonal',
                         alpha=.2)

map_LIM010103_wgs84.plot(color='yellow',
                         edgecolor = 'black',
                         ax = ax,
                         legend = 'Cicloruta',
                         alpha=.2)

map_LIM010104_wgs84.plot(color='blue',
                         edgecolor = 'black',
                         ax = ax,
                         legend = 'Via Principal',
                         alpha=.2)

map_LIM010105_wgs84.plot(color='red',
                         edgecolor = 'black',
                         ax = ax,
                         legend = 'Via Secundaria',
                         alpha=.2)

milano.plot(color='black',
            edgecolor = 'black',
            ax = ax,
            alpha=.1)

ax.set_title('Movilidad y Transporte\nMilano')
ax.set_axis_off()
plt.axis('equal');