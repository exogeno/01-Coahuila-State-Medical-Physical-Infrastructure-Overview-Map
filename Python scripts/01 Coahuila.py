# -*- coding: utf-8 -*-
"""
Created on Fri Apr  9 22:57:21 2021

@author: JOSECAL
"""
import geopandas as gpd
import matplotlib.pyplot as plt
import pysal as ps

help(gpd)
# Importing an ESRI Shapefile and plotting it using GeoPandas
estado = gpd.read_file(r'C:\Users\josecal\Documents\GEO-PROYECTOS\01 Coahila\Shapes\Estado\lim_estatal.shp')
type(estado)
municipios=gpd.read_file(r'C:\Users\josecal\Documents\GEO-PROYECTOS\01 Coahila\Shapes\Municipios\lim_mun.shp')
vias=gpd.read_file(r'C:\Users\josecal\Documents\GEO-PROYECTOS\01 Coahila\Shapes\Vias\vias.shp')
hospitales=gpd.read_file(r'C:\Users\josecal\Documents\GEO-PROYECTOS\01 Coahila\Shapes\Hospitales\hospitales.shp')
municipios.plot(cmap = 'viridis', edgecolor = 'black', column = 'NOM_MUN')
municipios.plot(color='none',edgecolor = 'black')
hospitales.plot()
anp=gpd.read_file(r'C:\Users\josecal\Documents\GEO-PROYECTOS\01 Coahila\Shapes\ANP\anp_coahuila.shp')
anp.plot()
#Plot the figures side by side
fig, (ax1, ax2) = plt.subplots(ncols= 2, figsize=(10,8))
municipios.plot(ax = ax1, cmap = 'magma', edgecolor = 'black', column = 'NOM_MUN')
vias.plot(ax = ax2, color = 'green')

fig, (ax1, ax2) = plt.subplots(nrows= 2, figsize=(10,8))
estado.plot(ax = ax1, color = 'none', edgecolor = 'black')
hospitales.plot(ax = ax2, color = 'black', markersize=(1))

fig, (ax1, ax2, ax3, ax4) = plt.subplots(ncols= 4, figsize=(50,40))
estado.plot(ax = ax1, color = 'none', edgecolor = 'black')
hospitales.plot(ax = ax2, color = 'blue', markersize=(50), marker='*')
vias.plot(ax = ax3, color = 'grey')
municipios.plot(ax = ax4, cmap = 'cool', edgecolor = 'black', column = 'NOM_MUN', alpha=0.5)
#Creating a legend
fig, ax = plt.subplots(1, 1)
municipios.plot(column='Area', ax=ax, legend=True,
legend_kwds={'label': "Area", 'orientation': "horizontal"})
# Plotting multiple layers
fig, ax = plt.subplots(figsize = (50,40))
municipios.plot(ax = ax, cmap = 'plasma', edgecolor = 'black', column = 'NOM_MUN')
estado.plot(ax = ax, color = 'none', edgecolor = 'black')
hospitales.plot(ax = ax, color = 'blue', markersize = 90)
vias.plot(ax = ax, color = 'black')
anp.plot(ax = ax, color = 'none', edgecolor = 'green')
municipios.crs #epsg:4326


# Reprojecting GeoPandas GeoDataFrames
municipios = municipios.to_crs(epsg = 32614)
estado = estado.to_crs(epsg = 32614)
hospitales = hospitales.to_crs(epsg = 32614)
vias = vias.to_crs(epsg = 32614)
anp= anp.to_crs(epsg = 32614)

# Plotting multiple layers 2
fig, ax = plt.subplots(figsize = (50,40))
municipios.plot(ax = ax, cmap = 'inferno', edgecolor = 'black', column = 'NOM_MUN')
estado.plot(ax = ax, color = 'none', edgecolor = 'black')
estado.plot(ax = ax, color = 'none', edgecolor = 'black')
hospitales.plot(ax = ax, color = 'blue', markersize = 90)
vias.plot(ax = ax, color = 'grey')

# Plotting multiple layers 3
fig, ax = plt.subplots(figsize = (60,40))
municipios.plot(ax = ax, color = 'black', edgecolor = 'grey', zorder=1)
estado.plot(ax = ax, color = 'none', edgecolor = 'red',zorder=5)
hospitales.plot(ax = ax, color = 'cyan',edgecolor = 'red', markersize = 190, zorder=4)
vias.plot(ax = ax, color = 'yellow',zorder=3)
anp.plot(ax = ax, color = 'green', edgecolor = 'magenta', zorder=2, alpha=0.4)

# Intersecting Layers
municipios_en_anp = gpd.overlay(municipios, anp, how = 'intersection')
municipios_en_anp.plot(color='green', edgecolor = 'red')

# Plotting multiple layers 3
fig, ax = plt.subplots(figsize = (60,40))
municipios.plot(ax = ax, color = 'black', edgecolor = 'white', zorder=1)
estado.plot(ax = ax, color = 'none', edgecolor = 'red',zorder=6, linewidth=10)
hospitales.plot(ax = ax, color = 'cyan',edgecolor = 'red', markersize = 190, zorder=5)
vias.plot(ax = ax, color = 'yellow',zorder=4)
anp.plot(ax = ax, color = 'green', edgecolor = 'magenta', zorder=2)
municipios_en_anp.plot(ax = ax, color='none', edgecolor = 'white',zorder=3)



# Calculating the areas of the intersected layer 
municipios_en_anp['area'] = municipios_en_anp.area/1000000

# Exporting GeoPandas GeoDataFrames
municipios_en_anp.to_file('municipios_en_anp.shp', driver = "ESRI Shapefile")





