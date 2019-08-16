import numpy as np
import pandas as pd
import geopandas as gp
import matplotlib as mpl
from matplotlib import cm
lon_0 = -139.4351
lon_1 = -52.6961
lat_0 = 42.0377
lat_1 = 70.4643
census = pd.read_csv('2011Census_FSA.csv')
age = census[census.Topic == 'Agecharacteristics'][['Geo_code', 'Characteristic', 'Total']]
age = pd.pivot_table(age, index = 'Geo_code', columns = 'Characteristic')
age.columns = age.columns.droplevel()
age['young'] = age[['0to4years', '5to9years', '10to14years', '15to19years', '20to24years', '25to29years', '30to34years',
    '35to39years', '40to44years', '45to49years', '50to54years', '55to59years', '60to64years']].sum(axis = 1)
age['old'] = age[['65to69years', '70to74years', '75to79years', '80to84years', '85yearsandover']].sum(axis = 1)
age['ratio'] = age['old'] / (age['old'] + age['young'])
space = gp.read_file("2011Cen_FSA.shp")
space.to_crs({'init': 'epsg:3395'})
age['CFSAUID'] = age.index.values
space = space.merge(age[['CFSAUID', 'ratio']], on = 'CFSAUID')
vmin = 0.0 #space.frac.min()
vmax = 0.30 #space.frac.max()
cmap = cm.hot
norm = mpl.colors.Normalize(vmin = vmin, vmax = vmax)
fig = space.plot(column = 'ratio', cmap = cmap, vmin = vmin, vmax = vmax, linewidth = 0.25)
mpl.pyplot.tight_layout()
bbx = fig.get_position()
axs = fig.get_figure()
aax = axs.add_axes([0.1, 0.1, 0.8, 0.03])
cb = mpl.colorbar.ColorbarBase(aax, cmap = cmap, norm = norm, orientation = 'horizontal')
cb.set_label('Fraction of population 65 years and older')
mpl.pyplot.savefig('census.png')
mpl.pyplot.close()
mpl.pyplot.clf()
