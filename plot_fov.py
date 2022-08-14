import jcoord
import numpy as n
import matplotlib.pyplot as plt
import h5py
import glob
import stuffr

import cartopy.crs as crs
import cartopy.feature as cfeature

#def get_gcd_grid():
 #   gc_dists= tt.great_circle(tonga_lon,tonga_lat, longg, latg)
  #  return(longg,latg,gc_dists)

sb_lat=78.17352651210611
sb_lon=16.00626276479981

ski_lat=69.34701844739395
ski_lon=20.289042789676095

def elsgrid(lat0,lon0,alt=100e3):
    lat_grid=n.linspace(59,90,num=100)
    lon_grid=n.linspace(-50,80,num=100)    
    longg,latg=n.meshgrid(lon_grid,lat_grid)
    els=n.copy(latg)
    for i in range(len(lat_grid)):
        for j in range(len(lon_grid)):
            az,el,r=jcoord.geodetic_to_az_el_r(lat0, lon0, 0, lat_grid[i], lon_grid[j], alt)
            els[i,j]=el
    return(longg,latg,els)

#longg,latg,els=elsgrid(sb_lat,sb_lon,alt=120e3)
#plt.pcolormesh(els)
#plt.colorbar()
#plt.show()

fig = plt.figure(figsize=(6,6))
prj=crs.AzimuthalEquidistant(central_longitude=sb_lat,central_latitude=sb_lon)#,false_easting=2000e3,false_northing=2000e3)
ax = plt.axes(projection=prj)
#ax.set_global()
#ax.set_extent([sb_lon-50,sb_lon+30,sb_lat-10,sb_lat+20], crs=crs.PlateCarree())
gl=ax.gridlines(crs=crs.PlateCarree(),draw_labels=True)
#gl.xlabels_top = False
#gl.ylabels_right = False
ax.coastlines()
ax.scatter(x=sb_lon,y=sb_lat,color="red",transform=crs.PlateCarree())

longg,latg,els_e=elsgrid(sb_lat,sb_lon,alt=120e3)
gcd_labels=[30]
line_c=ax.contour(longg,latg,els_e,levels=gcd_labels,transform=crs.PlateCarree(),colors=["green"])
# Use the line contours to place contour labels.
ax.clabel(
    line_c,  # Typically best results when labelling line contours.
    colors=['green'],
    manual=False,  # Automatic placement vs manual placement.
    inline=True,  # Cut the line where the label will be placed.
    fmt='120 km'.format,  # Labes as integers, with some extra space.
)


longg,latg,els_f=elsgrid(sb_lat,sb_lon,alt=300e3)
gcd_labels=[30]
line_c=ax.contour(longg,latg,els_f,levels=gcd_labels,transform=crs.PlateCarree(),colors=["red"])
# Use the line contours to place contour labels.
ax.clabel(
    line_c,  # Typically best results when labelling line contours.
    colors=['red'],
    manual=False,  # Automatic placement vs manual placement.
    inline=True,  # Cut the line where the label will be placed.
    fmt='300 km'.format,  # Labes as integers, with some extra space.
)
longg,latg,els_top=elsgrid(sb_lat,sb_lon,alt=800e3)
gcd_labels=[30]
line_c=ax.contour(longg,latg,els_top,levels=gcd_labels,transform=crs.PlateCarree(),colors=["blue"])
# Use the line contours to place contour labels.
ax.clabel(
    line_c,  # Typically best results when labelling line contours.
    colors=['blue'],
    manual=False,  # Automatic placement vs manual placement.
    inline=True,  # Cut the line where the label will be placed.
    fmt='800 km'.format,  # Labes as integers, with some extra space.
)


longg,latg,els_f_ski=elsgrid(ski_lat,ski_lon,alt=300e3)
gcd_labels=[30]
line_c=ax.contour(longg,latg,els_f_ski,levels=gcd_labels,transform=crs.PlateCarree(),colors=["red"])
# Use the line contours to place contour labels.
ax.clabel(
    line_c,  # Typically best results when labelling line contours.
    colors=['red'],
    manual=False,  # Automatic placement vs manual placement.
    inline=True,  # Cut the line where the label will be placed.
    fmt='300 km'.format,  # Labes as integers, with some extra space.
)

longg,latg,els_e_ski=elsgrid(ski_lat,ski_lon,alt=120e3)
gcd_labels=[30]
line_c=ax.contour(longg,latg,els_e_ski,levels=gcd_labels,transform=crs.PlateCarree(),colors=["green"])
# Use the line contours to place contour labels.
ax.clabel(
    line_c,  # Typically best results when labelling line contours.
    colors=['green'],
    manual=False,  # Automatic placement vs manual placement.
    inline=True,  # Cut the line where the label will be placed.
    fmt='120 km'.format,  # Labes as integers, with some extra space.
)
longg,latg,els_top_ski=elsgrid(ski_lat,ski_lon,alt=800e3)
gcd_labels=[30]
line_c=ax.contour(longg,latg,els_top_ski,levels=gcd_labels,transform=crs.PlateCarree(),colors=["blue"])
# Use the line contours to place contour labels.
ax.clabel(
    line_c,  # Typically best results when labelling line contours.
    colors=['blue'],
    manual=False,  # Automatic placement vs manual placement.
    inline=True,  # Cut the line where the label will be placed.
    fmt='800 km'.format,  # Labes as integers, with some extra space.
)

plt.savefig("esr.pdf")
plt.show()
