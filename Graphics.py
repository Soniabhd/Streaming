#Graphics

import os
import pandas as pd
import plotly.graph_objects as go

path = os.getcwd()
ap = pd.read_csv(path+"\\amazon_prime_titles.csv",sep = ",",low_memory=False)
dp = pd.read_csv(path + "\\disney_plus_titles.csv",sep = ",",low_memory=False)
hu = pd.read_csv(path + "\\hulu_titles.csv",sep = ",",low_memory=False)
nf = pd.read_csv(path + "\\netflix_titles.csv",sep = ",",low_memory=False)

x = ["TV Show","Movie",'Total']

y = [len(ap[ap['type']=='TV Show']),len(ap[ap['type']=='Movie']),ap.shape[0]]
y2 = [len(dp[dp['type']=='TV Show']),len(dp[dp['type']=='Movie']),dp.shape[0]]
y3 = [len(nf[nf['type']=='TV Show']),len(nf[nf['type']=='Movie']),nf.shape[0]]
y4 = [len(hu[hu['type']=='TV Show']),len(hu[hu['type']=='Movie']),hu.shape[0]]

fig = go.Figure()
fig.add_trace(go.Histogram(histfunc = 'sum', y=y, x=x, name="Amazon Prime",marker_color='#a669f7'))
fig.add_trace(go.Histogram(histfunc = 'sum', y=y2, x=x, name="Disney Plus",marker_color='#61d2f1'))
fig.add_trace(go.Histogram(histfunc = 'sum', y=y3, x=x, name="Netflix",marker_color='#ef6b94'))
fig.add_trace(go.Histogram(histfunc = 'sum', y=y4, x=x, name="Hulu",marker_color='#bde684'))

fig.show()