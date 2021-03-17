"""Example 1-1 from *Hands On Machine Learning* by Aurelien Geron.

It combines 2016 OECD data on Life Satisfaction, combined with GDP data
from the IMF World Economic Outlook Database, April 2016.  The data has
been pre-processed from the links given in the text, in the interest of
keeping hardcopy space to a minimum.
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
from sklearn import linear_model as lm
from scipy.stats import linregress as lr

def ETL(OECD, IMF, post = False):
    """Extract-Transform-Load pipeline for raw files from textbook.

    The original data files were processed in the following manner
    before being stored on the hard drive.  The steps are listed here
    for reproducability reasons.

    Arguments
    ---------
    OECD : str
        The file path to the OECD data.
    IMF : str
        The file path to the IMF data.

    Keywords
    --------
    post : boolean
        Whether the file pre-processing needs to be re-run.

    Returns
    -------
    df : ~pandas.DataFrame
        The inner join between the two DateFrames for model fitting.
    """
    def _map(x):
        if isinstance(x, float):
            return float(x)
        else:
            return float(x.replace(',',''))
    if post:
        imf = pd.read_table(IMF, encoding = 'latin1')
        imf.drop(189, axis = 0, inplace = True) # drop the tag line
        imf = imf[['Country', '2015']] # replace with proper year if needed
        imf.columns = ['Country', 'GDPC']
        imf['GDPC'] = imf['GDPC'].replace('n/a',np.NaN)
        imf['GDPC'] = imf['GDPC'].map(lambda x: _map(x))

        oecd = pd.read_csv(OECD, encoding = 'latin1')
        oecd = oecd[(oecd['INEQUALITY'] == 'TOT') & (oecd['INDICATOR'] == 'SW_LIFS')][['Country',
            'Value']]
        oecd.reset_index(drop = True, inplace = True)
        oecd.columns = ['Country', 'LI']
    
    else:

        imf = pd.read_csv(IMF, encoding = 'latin1')
        oecd = pd.read_csv(OECD, encoding = 'latin1')

    return oecd.merge(imf, on = 'Country', how = 'inner')

nf = fm.FontProperties(fname = '/Library/Fonts/Comic Sans MS.ttf', size = 7)
bf = fm.FontProperties(fname = '/Library/Fonts/Comic Sans MS Bold.ttf', size = 7)

df = ETL('DATA/OECD.csv', 'DATA/IMF.csv')
df.reset_index(drop = True, inplace = True)

# Converts the length M vectors into Mx1 matrices.  Similar to using `~numpy.reshape(1,M)`
X = np.c_[df['GDPC']]
y = np.c_[df['LI']]

cl = ['South Africa', 'Portugal', 'Czech Republic', 'Italy', 'France', 'United States',
    'Switzerland', 'Norway', 'Luxembourg']
yf = [-20, -8, 5, -8, -8, -20, -15, 10, 5]

LRM = lm.LinearRegression()
LRM.fit(X, y)
theta = [LRM.intercept_[0], LRM.coef_[0][0]]

m, b, r, p, dm = lr(df['GDPC'].values, df['LI'].values)
beta = [b, m]

x = np.linspace(0, 1e5, 100)

fig, ax = plt.subplots(figsize = (8, 5))
ax.scatter(df.GDPC.values, df.LI.values, color = 'blue', s = 10)
ax.plot(x, theta[0] + theta[1] * x, color = 'red', ls = '-', lw = 1.5)

ax.set_xlabel('GDP per Capita [USD]', fontproperties = bf)
ax.set_ylabel('Life Happines Index', fontproperties = bf)
ax.set_ylim(4.5, 8.5)

kwargs = dict(xycoords = 'data', textcoords = 'offset points', fontproperties = nf, ha = 'center')
for c,y in zip(cl, yf):
    i = df[df.Country == c].index.values[0]
    kwargs['xytext'] = (0, y)
    txt = df.iloc[i].Country.replace(' ','\n')
    ax.annotate(txt, xy = (df.iloc[i].GDPC, df.iloc[i].LI), **kwargs)

for t in ax.get_xticklabels():
    t.set_fontproperties(nf)
for t in ax.get_yticklabels():
    t.set_fontproperties(nf)

ax.patch.set_alpha(0.0)
fig.patch.set_alpha(0.0)
plt.savefig('ex1-1_linear_model_sklearn.png', dpi = 300)
plt.clf()
plt.close()
print('Linear Model:', theta)
print('Linear Regression:', beta)
